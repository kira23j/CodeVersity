// list data type in dart and some common methods.
void main() {
  // creation of a list with values.
  var listOne = [1, 2, 3, 4, 5];
  print(listOne);
// create an empty list.
  var emptyList = [];
  print(emptyList.length);
  // add a single value to empty list.
  emptyList.add(3);
  print(emptyList);
  // add a list of numbers to empty list.
  emptyList.addAll([6, 9]);
  print(emptyList);
  // insert a given value at index (i,v).
  emptyList.insert(1, 4);
  print(emptyList);
  // insert list values at a given index.
  emptyList.insertAll(3, [7, 8]);
  print(emptyList);
  // remove a value from list.
  emptyList.remove(9);
  print(emptyList);
  // remove a value at index.
  emptyList.removeAt(2);
  print(emptyList);
}
