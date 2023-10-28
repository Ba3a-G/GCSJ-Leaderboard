import Confetti from "react-confetti";
import useWindowSize from "react-use/lib/useWindowSize";
import React, { useState } from "react";
import axios from "axios";

const loadLeaderboard = async () => {
  try {
    var rawLeaderboard = await axios.get('https://csjprogress.s3.ap-south-1.amazonaws.com/leaderboard.json');
  } catch(err) {
    console.error('Couldn\'t load leaderboard.')
    return []
  }

  var leaderboard = [];
  var count = 1;
  rawLeaderboard.data.forEach((element) => {
    let participant = {
        name: element.userName,
        score: element.totalBadges,
        rank: count
    };
    leaderboard.push(participant);
    count+=1;
  });
  return leaderboard;
}

const leaderboards = await loadLeaderboard();

const Leaderboard = () => {
  const [isShown, setIsShown] = useState(false);
  const { width, height } = useWindowSize();

  return (
    <div className="bg-orange-100 py-10 sm:py-32 ">
      <Confetti
        width={width - 20}
        height={height + 800}
        numberOfPieces={800}
        recycle={false}
        tweenDuration={10000}
      />
      {isShown && (
        <Confetti
          width={width - 20}
          height={height + 500}
          recycle={false}
          numberOfPieces={100}
          tweenDuration={10000}
        />
      )}
      <h2 className="text-5xl text-center font-bold tracking-tight text-gray-900 sm:text-7xl mb-12">
        <span className="text-7xl block pb-4">📜</span>Study Jams Leaderboard
      </h2>

      <div className="mx-auto  max-w-7xl px-6 lg:px-8">
        <div class="flex flex-wrap pt-20 gap-y-16 sm:flex-row mx-auto sm:gap-x-8 justify-center align-center py-10 ">
          {leaderboards.map((leaderboard) => {
            if (leaderboard.rank === 2) {
              return (
                <div
                  onMouseEnter={() => setIsShown(true)}
                  onMouseLeave={() => setIsShown(false)}
                  className="sm:order-1 order-2 flex flex-col items-center shadow-lg hover:shadow-2xl w-60 bg-orange-200 rounded-xl p-2 transform transition-all hover:-translate-y-2 duration-300"
                >
                  <div className="flex items-center gap-x-2 pt-2 ">
                    <h2 className="text-9xl relative -top-12">🥈</h2>
                  </div>

                  <h2 className="pt-8 text-2xl ">{leaderboard.name}</h2>

                  <h2 className=" px-2 font-bold py-2">
                    Score : {leaderboard.score}
                  </h2>
                </div>
              );
            }

            if (leaderboard.rank === 1) {
              return (
                <div
                  onMouseEnter={() => setIsShown(true)}
                  onMouseLeave={() => setIsShown(false)}
                  className="order-2 relative sm:-top-10 flex flex-col items-center shadow-lg hover:shadow-2xl w-60 bg-orange-200 rounded-xl p-2 transform transition-all hover:-translate-y-2 duration-300"
                >
                  <div className="flex items-center gap-x-2 pt-2 ">
                    <h2 className="text-9xl relative -top-12">🏆</h2>
                  </div>

                  <h2 className="pt-8 text-2xl ">{leaderboard.name}</h2>

                  <h2 className=" px-2 font-bold py-2">
                    Score : {leaderboard.score}
                  </h2>
                </div>
              );
            }

            if (leaderboard.rank === 3) {
              return (
                <div
                  onMouseEnter={() => setIsShown(true)}
                  onMouseLeave={() => setIsShown(false)}
                  className="order-3 flex flex-col items-center shadow-lg hover:shadow-2xl w-60 bg-orange-200 rounded-xl p-2 transform transition-all hover:-translate-y-2 duration-300"
                >
                  <div className="flex items-center gap-x-2 pt-2 ">
                    <h2 className="text-9xl relative -top-12">🥉</h2>
                  </div>

                  <h2 className="pt-8 text-2xl ">{leaderboard.name}</h2>

                  <h2 className=" px-2 font-bold py-2">
                    Score : {leaderboard.score}
                  </h2>
                </div>
              );
            }
          })}
        </div>
      </div>
      <div className="mx-auto max-w-7xl lg:px-8 ">
        <div className="w-5/6 sm:w-4/5 flex flex-col gap-y-6 mx-auto justify-center align-center my-10 ">
          {leaderboards.map((leaderboard) => {
            if (leaderboard.rank > 3) {
              return (
                <div className="flex flex-row place-content-between items-center shadow-lg hover:shadow-2xl  bg-orange-200 rounded-xl py-2 px-4 transform transition-all hover:-translate-y-2 duration-300">
                  <p className="font-bold p-3">{leaderboard.rank}</p>

                  <p className="p-3 ">{leaderboard.name}</p>

                  <p className="p-3 font-bold">{leaderboard.score}</p>
                </div>
              );
            }
          })}
        </div>
      </div>
    </div>
  );
};
export default Leaderboard;
