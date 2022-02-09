@echo off

cd ..

echo creating logs
mkdir logs

echo creating logs/commands.log
touch logs/commands.log

echo creating bot/resources/temp
mkdir bot/resources/temp

echo creating config.yaml
touch config.yaml

echo creating bot/utils/node
mkdir bot/utils/node

echo cloning TMIndiaBotApi
git clone https://github.com/TrackmaniaIndia/TMIndiaBotApi.git bot/utils/node/TMIndiaBotApi

echo cloning TrackmaniaLeaderboards
git clone https://github.com/NottCurious/TrackmaniaLeaderboards.git bot/resources/leaderboard
