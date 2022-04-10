int main(){
    // Test ARGUMENT
    int result = 0;
    // Test VARIABLE
    int temp = 0;
    // Test FOR LOOP
    for (int i = 0; i < 5; i++) {
        temp = i/3;
        // Test IF + EXPRESSION
        if( (temp == 0)
            // Test STATEMENT
            result += 1;
    }
    int k = 6;
    // Test IF + EXPRESSION
    if (result >= temp){
        // Test WHILE LOOP
        while (k > 3) {
            // Test STATEMENT
            result *= k;
            k--;
        }
    }
    else {
        result = 10;
    }
}