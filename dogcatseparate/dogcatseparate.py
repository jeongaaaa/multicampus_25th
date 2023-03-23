#폴더 만들어서 이미지 파일 복사하는 코드 만들어보기

#1. 이미지가 저장된 폴더의 문자열 변수 생성

srcPath = '/Users/jeonga/python_practice/train/'

import os
import glob
import shutil

#srcPath의 파일 목록 읽어오기
filenames = os.listdir(srcPath)

#폴더 내의 파일 개수 확인도 가능
print(len(filenames))

#위치 절대경로로 지정해서 폴더 만들기

dirname1 = srcPath + 'dog'
dirname2 = srcPath + 'cat'
os.makedirs(srcPath, exist_ok=True)
os.makedirs(srcPath, exist_ok=True)

#glob 모듈을 사용하면 jpg파일만 골라낼 수 있음
jpgFile = glob.glob(srcPath+'*.jpg')

#파일명만 추출해주는 함수 활용
for src in jpgFile:
    baseFileName = os.path.basename(src)
    category,_,_ = baseFileName.split('.')
    dst = srcPath + category + '/' + baseFileName
    shutil.copy(src, dst)
