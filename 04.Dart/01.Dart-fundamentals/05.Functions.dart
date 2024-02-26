void main() {
  // create function with parameter , [] use it for positional parameter , use {} for named parameters.

  animeDesc(String name, {genre = "default"}) {
    return "Anime name is $name and its genre is $genre";
  }

  String anime1 = "class room of the elite";
  String genre1 = "pyschology";
  print(animeDesc(anime1, genre: genre1));
  print(animeDesc("death note"));
}
