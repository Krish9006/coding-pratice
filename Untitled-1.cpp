#include <bits/stdc++.h>
using namespace std;
#define f(i, start, end) for (int i = start; i < end; i++)
#define fs(i, start, end, step) for (int i = start; i < end; i += step)
#define fr(i, start, end) for (int i = start; i > end; i--)
#define all(arr) arr.begin(), arr.end()
#define vi vector<int>
#define vvi vector<vi>
#define YES cout << "YES" << endl;
#define NO cout << "NO" << endl;
#define p(x) cout << (x) << endl;
#define sp(x) cout << (x) << " ";
#define endl '\n'
#define vlli vector<long long int>
#define mxv(arr) *max_element(arr.begin(), arr.end())
#define mnv(arr) *min_element(arr.begin(), arr.end())
#define smv(arr) accumulate(arr.begin(), arr.end(), 0LL)
#define srt(arr) sort(arr.begin(), arr.end())
#define rev(arr) reverse(all(arr))
#define MOD2 1000000007
#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)
typedef long long lli;

void solve() {
    int n, m; 
    cin >> n >> m;
    string s; 
    cin >> s;
    vi v(m); 
    f(i, 0, m){
        cin >> v[i];
    }
    string c; 
    cin >> c;
    set<int>st;
    f(i, 0, m){
        st.insert(v[i]);
    }
    vi ans(m);
    int idx = 0;
    for(auto it : st){
        ans[idx++] = it;
    }
    srt(c);
    idx = 0;
    f(i, 0, m){
        s[ans[i]-1] = c[idx++];
    }
    cout<<s<<endl;
}

int main() {
    fastio;
    int t; 
    cin >> t;
    while (t--)
        solve();
}