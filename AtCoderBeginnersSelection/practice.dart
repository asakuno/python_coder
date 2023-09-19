// 高橋君はデータの加工が行いたいです。

// 整数 a,b,cと、文字列 s が与えられます。 
// a+b+c の計算結果と、文字列 s を並べて表示しなさい。

import 'dart:io';

void main () {
  final input = stdin.readLineSync();
  final a = int.tryParse(input ?? '');

  
  final inputs = stdin.readLineSync()?.split(" ").map(int.tryParse).toList();
  final b = inputs?[0];
  final c = inputs?[1];

  final gets = stdin.readLineSync();
  final s = gets ?? '';

  print((a ?? 0) + (b ?? 0) + (c ?? 0));
  print(s);
}