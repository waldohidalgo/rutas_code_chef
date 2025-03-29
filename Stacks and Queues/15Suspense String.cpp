#include <iostream>
#include <deque>
#include <string>

using namespace std;

void alice(deque<char>& s, deque<char>& t) {
    char chr = s.front();
    
    s.pop_front();
    if (!t.empty() && chr == '0') {
        t.push_front(chr);
    } else {
        t.push_back(chr);
    }
}

void bob(deque<char>& s, deque<char>& t) {
    char chr = s.back();
    s.pop_back();
    if (!t.empty() && chr == '1') {
        t.push_front(chr);
    } else {
        t.push_back(chr);
    }
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        string s;
        cin >> s;
        
        deque<char> q(s.begin(), s.end());
        deque<char> t;
        
        int i = 0;
        while (!q.empty()) {
            if (i % 2 == 0) {
                alice(q, t);
            } else {
                bob(q, t);
            }
            i++;
        }
        
        for (char c : t) {
            cout << c;
        }
        cout << "\n";
    }
    return 0;
}
