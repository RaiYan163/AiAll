
#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
     Function to return Breadth First Traversal of given graph.
    vector<int> bfsOfGraph(int V, vector<int> adj[]) {
        int st_node = 0;  
        map<int, bool> check;
        vector<int> ans;
        queue<int> q;
        check[0] = true;  
        q.push(0);

        while (!q.empty()) {
            int x = q.front();

            q.pop();
            ans.push_back(x);  

            for (int i = 0; i < adj[x].size(); i++) {
                int c = adj[x][i];
                if (!check[c]) {
                    check[c] = true;
                    q.push(c);
                }
            }
        }

        return ans;
    }
};

//{ Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int V, E;
        cin >> V >>

            E;

        vector<int> adj[V];

        for (int i = 0; i < E; i++) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            // 		adj[v].push_back(u);
        }
        // string s1;
        // cin>>s1;
        Solution obj;
        vector<int> ans = obj.bfsOfGraph(V, adj);
        for (int i = 0; i < ans.size(); i++) {
            cout << ans[i] << " ";
        }
        cout << endl;
    }
    return 0;
}
// } Driver Code Ends