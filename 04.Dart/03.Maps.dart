// a map is what we call dictionary in python.
void main() {
  var programming = {
    "name": "dart",
    "framework": "Flutter",
    "owner": "Google",
    "yearOfPub": 2017
  };
  print(programming);
  print(programming.length);
  // print keys and values separately.
  print(programming.values);
  print(programming.keys);
  // add other key values pairs
  programming.addAll({"usage": "cross-platform Applications"});
  print(programming);
  // remove and clear the map
  programming.remove("usage");
  print(programming);
  programming.clear();
  print(programming);
}
