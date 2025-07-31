class Solution {
public:
    int countOdds(int low, int high) {
        // This is the direct conversion of your Python logic.
        // If the span between low and high is even, the number of odds and evens is the same.
        // If the span is odd, one is more frequent. We check if the boundaries are odd.
        int span = high - low;
        if (low % 2 != 0 || high % 2 != 0) {
            return span / 2 + 1;
        } else {
            return span / 2;
        }
    }
};