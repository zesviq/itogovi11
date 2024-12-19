Remove-Item -Recurse -Force ./dist/main

pyinstaller main.pyw

# cd dist/main/
# ./main.exe

./dist/main/main.exe