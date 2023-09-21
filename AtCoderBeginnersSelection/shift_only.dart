// 黒板に N 個の正の整数 A1,...,ANが書かれています．
// すぬけ君は，黒板に書かれている整数がすべて偶数であるとき，次の操作を行うことができます．

// 黒板に書かれている整数すべてを2で割ったものに置き換える．
// すぬけ君は最大で何回操作を行うことができるかを求めてください．

import 'dart:io';
import 'dart:math';

void main() {
  const int divisor = 2;

  final input = stdin.readLineSync();
  final n = int.tryParse(input ?? '');

  final numbers = stdin.readLineSync()?.split(" ").map(int.parse).toList() ?? [];

  final counts = [];
  for (int i = 0; i < numbers.length; i++) {
    int count = 0;

    while (numbers[i] % divisor == 0) {
      numbers[i] ~/= divisor; 
      count++;
    }
    counts.add(count);
  }
  print(counts.reduce((a, b) => a < b ? a : b));
}