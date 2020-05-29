class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int res = 0;
        for(int i=0;i<grid.size();i++)
        {
            for(int j=0;j<grid[0].size();j++)
            {
                if(grid[i][j]=='1')
                {
                    res++;
                    helper(grid,i,j);
                }
            }
        }
        return res;
    }
    void helper(vector<vector<char>>& grid,int i,int j)
    {
        if(i<0 || i>=grid.size() || j<0 || j>=grid[0].size() || grid[i][j]=='0')
            return;
        grid[i][j]='0';
        // 上 下 左 右         
        helper(grid,i-1,j);
        helper(grid,i+1,j);
        helper(grid,i,j-1);
        helper(grid,i,j+1);
    }
};