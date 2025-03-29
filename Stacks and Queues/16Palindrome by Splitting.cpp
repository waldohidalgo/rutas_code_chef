#include <iostream>
#include <deque>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        deque<int> q(n);
        for (int j = 0; j < n; j++) {
            cin >> q[j];
        }
        int count = 0;
        while (q.size() > 0) {
            int l = q.front();
            int r = q.back();
            if (l < r) {
                count++;
                int diff = r - l;
                q.pop_front();
                q.pop_back();
                q.push_back(diff);
            } else if (l > r) {
                count++;
                int diff = l - r;
                q.pop_front();
                q.pop_back();
                q.push_front(diff);
            } else {
                q.pop_front();
                if (q.size() > 0) {
                    q.pop_back();
                }
            }
        }
        cout << count << "\n";
    }
    return 0;
}
