echo $1
export API_KEY=$1
# get the first bucket name and store it in a variable
bucket_name=$(gsutil ls | head -n 1)
echo $bucket_name
# make all contents of the bucket public
gsutil acl set -r public-read $bucket_name
# get image name from bucket
image_name=$(gsutil ls $bucket_name | head -n 1)
echo "{\"requests\":[{\"image\":{\"source\":{\"gcsImageUri\":\"$bucket_name/manif-des-sans-papiers.jpg\"}},\"features\":[{\"type\":\"TEXT_DETECTION\",\"maxResults\":10}]}]}" >> text.json
curl -s -X POST -H "Content-Type: application/json" --data-binary @text.json https://vision.googleapis.com/v1/images:annotate?key=$1 -o text-response.json
gsutil cp text-response.json $bucket_name
echo "{\"requests\":[{\"image\":{\"source\":{\"gcsImageUri\":\"$bucket_name/manif-des-sans-papiers.jpg\"}},\"features\":[{\"type\":\"LANDMARK_DETECTION\",\"maxResults\":10}]}]}" >> landmark.json
curl -s -X POST -H "Content-Type: application/json" --data-binary @landmark.json  https://vision.googleapis.com/v1/images:annotate?key=$1 -o landmark-response.json
gsutil cp landmark-response.json $bucket_name