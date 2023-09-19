import 'dart:io';

void main() {
  // 入力値が一行に一つだけ
  // final x = int.parse(stdin.readLineSync());

  // // 入力値が空白区切りで固定数
  // final inputs = stdin.readLineSync().split(" ").map(int.parse).toList();
  // final x = inputs[0];
  // final y = inputs[1];
  // final z = inputs[2];

  // // ２つだけならtoListはなくてもいい
  // final inputs = stdin.readLineSync().split(" ").map(int.parse);
  // final x = inputs.first;
  // final y = inputs.last;

  // // 文字が多いとき
  // final lines = stdin.transform(utf8.decoder).transform(LineSplitter());

  // await for (final line in lines) {
    
  // }
}
//絶対値
// num.abs()

// ソート
// List.sort((a, b) => a - b) で昇順ソート
// b - a にすると降順ソートになる

// 文字列切り出し
// String.substring(start, end)
// abcdefghi の f は6文字目。 substring(0, 6) => abcdef

// 偶奇判定
// int.isEven / int.isOdd で判定可能
// ２つの数の偶奇が一致するかどうかは a %2 == b % 2 で見たほうがよい

// 畳み込み系
// Iterable.reduce((prev, value) => prev + value) 初期値がいらない
// Iterable.fold(true, (prev, value) => prev && value) 初期値がいる