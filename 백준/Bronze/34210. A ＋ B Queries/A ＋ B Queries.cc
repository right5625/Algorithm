#include "aplusb.h"
#include <vector>

static std::vector<int> A1;
static std::vector<int> B1;

void initialize(std::vector<int> A, std::vector<int> B) {
  A1 = A;
  B1 = B;
}

int answer_question(int i, int j) {
  return A1[i] + B1[j];
}
