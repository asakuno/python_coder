// シカのAtCoDeerくんは二つの正整数 a,b を見つけました。 
//a と b の積が偶数か奇数か判定してください。

import 'dart:io';

void main () {
  final inputs = stdin.readLineSync()?.split(" ").map(int.tryParse).toList();
  final a = inputs?[0];
  final b = inputs?[1];
}