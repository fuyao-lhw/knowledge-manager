#!/bin/bash

# 进入 Vue 3 项目目录并打包
cd front/perkm
npm install
npm run build

# 将打包后的文件复制到 Flask 项目的静态目录
cd ../../backend/perkm
mkdir -p static
cp -r ../../front/perkm/dist/* static/