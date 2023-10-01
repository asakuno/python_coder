// あなたは、500 円玉を A 枚、100 円玉を B 枚、50 円玉を C 枚持っています。 
// これらの硬貨の中から何枚かを選び、合計金額をちょうど X 円にする方法は何通りありますか。
// 同じ種類の硬貨どうしは区別できません。
// 2 通りの硬貨の選び方は、ある種類の硬貨についてその硬貨を選ぶ枚数が異なるとき区別されます。
import 'dart:io';
void main() {
  final int A = int.tryParse(stdin.readLineSync() ?? '0') ?? 0;
  final int B = int.tryParse(stdin.readLineSync() ?? '0') ?? 0;
  final int C = int.tryParse(stdin.readLineSync() ?? '0') ?? 0;
  final int X = int.tryParse(stdin.readLineSync() ?? '0') ?? 0;

  // for文を３回回す。
  var cnt = 0;
  for(int i = 0; i <= A; i++ ) {
    for(int j = 0; j <= B; j++) {
      for(int k = 0; k <= C; k++){
        if(500*A + 100*B + 50*C == X){
          cnt+=1;
        }
      }
    }
  }
  print(cnt);
}