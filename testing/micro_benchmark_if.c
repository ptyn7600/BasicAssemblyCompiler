int main() {
    int x = 5;
    int result1 = 0;
    int result2 = 0;
    // First If: Expression label - const
    if (x > 3) {
        result1 = 1;
    }
     // Second If: Expression const - const
    if (4 > 3) {
        result1 = 2;
    }
     // Third If: Expression const - label
    if (6 > x) {
        result1 = 10;
    }
     // Fourth If: Expression label - label
    if (x > result1) {
        result1 = 3;
    }
    else {
        result2 = 4;
    }
}