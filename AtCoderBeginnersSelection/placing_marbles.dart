// すぬけ君は 1,2,3 の番号がついた 3 つのマスからなるマス目を持っています。 
// 各マスには 0 か 1 が書かれており、マス i には s iが書かれています。
// すぬけ君は 1 が書かれたマスにビー玉を置きます。 
// ビー玉が置かれるマスがいくつあるか求めてください。

import 'dart:io';

void main() {
  final string = stdin.readLineSync();
  // 文字列の長さを定数に置く
  final stringRange = string?.length;
  // カウントする用の定数cntの定義
  var cnt = 0;
  // 文字列の長さ分for文で回す
  for(int i = 0; i < stringRange!; i++ ){
    if(string?[i] == '1') {
      // もし1の場合cnt+=1
      cnt+=1;
    }
  }
  print(cnt);
}