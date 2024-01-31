void main() {
  var a, b, c, d, e;
  a = 20;
  b = "3";
  c = "0.23";

  // string to int
  b = int.parse(b);
  // string to double
  c = double.parse(c);

  d = a + b + c;
  print("the sum of $a, $b, $c is $d");

  // int to string
  a = a.toString();
  // double to string
  d = d.toString();

  e = a + d;
  print("concat $a and $d :$e");
}
