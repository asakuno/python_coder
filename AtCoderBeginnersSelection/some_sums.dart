// 1 以上 N 以下の整数のうち、10 進法での各桁の和が A 以上 B 以下であるものの総和を求めてください。
import 'dart:io';

void main() {
  final inputs = stdin.readLineSync()?.split(" ").map(int.tryParse).toList();
  final n = inputs?[0];
  final a = inputs?[1];
  final b = inputs?[2];

  final array = <int>[];
  for(int i = 0; i <= 20; i++){
    final sum = splits(i).reduce((p,n) => p+n);
    if ((a ?? 0) <= sum && sum <= (b ?? 0)){
      array.add(i);
    }
  }
  print(array.reduce((p,n) => p + n));
}

List<int> splits(int i){
  final array = <int>[];
  for(int j = 0; j <= i; j++) {
    final above = i ~/ (j * 10);
    array.add((i - (above * j * 10)) ~/ j);
  }
  return array;
}