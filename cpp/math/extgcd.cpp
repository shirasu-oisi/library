// non-recursion
#include <utility>
auto extgcd(int a, int b){
  if(a<=b){ // swap
    int t{b};
    b = a;
    a = t;
  }

  int d{a / b};
  int p{0}, q{1}, r{1}, s{-d};
  while(a%b){
    int nb{a - b * d};
    a = b;
    b = nb;
    d = a / b;
    int nr{p - r * d}, ns{q - s * d};
    p = r;
    q = s;
    r = nr;
    s = ns;
  }
  return std::make_pair(p, q);
}


/*
#include <iostream>
int main() {
  auto res = extgcd(111, 30);
  std::cout << res.first << ' ' << res.second << std::endl; // 3 -11
}
*/