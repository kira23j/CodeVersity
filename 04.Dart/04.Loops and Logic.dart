void main() {
  var num = 10;
// for loop in dart
  for (var i = num; i >= 0; i--) {
    if (i % 2 == 1) {
      print("$i: odd");
    } else {
      print("$i: even");
    }
  }

// for in loops in dart.
  var cities = ["bahirdar", "addiss ababa", "debrebirhan"];
  print("cities in ethiopia");
  for (var city in cities) {
    print(city);
  }

// while loop in dart.
  var temp = [];
  while (num >= 0) {
    if (num % 2 == 0) {
      temp.add(num);
    }
    num--;
  }
  print("even numbers upto 10: $temp");
}
