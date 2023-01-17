//////////// Trick Solution //////////////

class Solution {
public:
    int minFlipsMonoIncr(string s) {
        int no_of_one =0;
        int flip = 0;
        
        for(auto ch:s){
            if(ch=='1'){
                no_of_one +=1;
            }
            else{
                flip = min(flip+1, no_of_one);
            }
        }
            return flip;
            
    }
};

/////////////////////// Memoziation ///////////////////////////

class Solution {
public:
    int n;
    int solve(string &s, int curr_index, int prev, vector<vector<int>> &t){
        if(curr_index>= n)
            return 0;
        int flip = INT_MAX;
        int noflip = INT_MAX;
        
        if(t[curr_index][prev] != -1){
            return t[curr_index][prev];
        }
        
        if(s[curr_index] == '0'){
            if(prev == 1){
                flip = 1 + solve(s, curr_index+1,1,t);
               
            }
            else{
                flip = 1 + solve(s,curr_index+1,1,t);
                noflip = solve(s, curr_index+1,0,t);
            }
        }
        else if(s[curr_index] == '1'){
            if(prev == 1){
                noflip= solve(s, curr_index+1,1,t);
            }
            else{
                flip = 1+solve(s, curr_index+1,0,t);
                noflip = solve(s, curr_index+1,1,t);
            }
        }
            
        return t[curr_index][prev] = min(noflip, flip);
            
    }
    
    
    
    int minFlipsMonoIncr(string s) {
        n = s.length();
        
        vector<vector<int>> t(n+1, vector<int>(2,-1));
        return solve(s,0,0,t);
        
        
    }
};


//////////////////// Recursive (Time Limit Exceed) ///////////////////////

class Solution {
public:
    int n;
    int solve(string &s, int curr_index, int prev){
        if(curr_index>= n)
            return 0;
        int flip = INT_MAX;
        int noflip = INT_MAX;
        if(s[curr_index] == '0'){
            if(prev == 1){
                flip = 1 + solve(s, curr_index+1,1);
               
            }
            else{
                flip = 1 + solve(s,curr_index+1,1);
                noflip = solve(s, curr_index+1,0);
            }
        }
        else if(s[curr_index] == '1'){
            if(prev == 1){
                noflip= solve(s, curr_index+1,1);
            }
            else{
                flip = 1+solve(s, curr_index+1,0);
                noflip = solve(s, curr_index+1,1);
            }
        }
            
        return min(noflip, flip);
            
    }
    
    
    
    int minFlipsMonoIncr(string s) {
        n = s.length();
        
        return solve(s,0,0);
        
        
    }
};

