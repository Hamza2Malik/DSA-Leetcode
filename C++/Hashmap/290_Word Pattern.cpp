/////////////////////// Approach 1/////////////////////////////
class Solution {
public:
   bool wordPattern(string pattern, string s)
{
     int cnt = 0;
     vector<string> temp;
     for (int i = 0; i < s.size(); i++)
     {
          string str;
          while (s[i] != ' ' && i < s.size())
          {
               str.push_back(s[i]);
               i++;
          }
          cnt++;
          temp.push_back(str);
     }
     if (cnt != pattern.size())
     {
          return false;
     }
     unordered_map<string, char> map;
     set<char> count;
     for (int i = 0; i < pattern.size(); i++)
     {
          if (map.find(temp[i]) == map.end() && count.find(pattern[i]) == count.end())
          {
               count.insert(pattern[i]);
               map.emplace(temp[i], pattern[i]);
          }
          else if (map[temp[i]] != pattern[i])
          {
               return false;
          }
     }
     return true;
}
};

/////////////////////// Approach 2////////////////////////////////

class Solution {
public:
  bool wordPattern(string pattern, string s) {
        vector<string> temp;
        stringstream ss(s);
        string token;
        int count = 0;
        while(getline(ss, token, ' ')) {
            temp.push_back(token);
            count++;
        }
         
         int n = pattern.size();
        
         if (count != n) 
             return false;
        
         unordered_map<string, char> mp;
         set<char> used;
         for (int i = 0; i < n; i++)
         {
              if (mp.find(temp[i]) == mp.end() && used.find(pattern[i]) == used.end()) {
                   used.insert(pattern[i]);
                   mp[temp[i]] = pattern[i];
              }
              else if (mp[temp[i]] != pattern[i]) {
                   return false;
              }
         }
         return true;
    }};

////////////////////// Apporach 3///////////////////////////////

class Solution {
public:
 bool wordPattern(string pattern, string s) {
        unordered_map<char, int> charToIndex;
        unordered_map<string, int> wordToIndex;
        
        stringstream ss(s);
        string token;
        int countTokens = 0;
        int i = 0; 
        int n = pattern.size();
        
        while(ss >> token) {
            countTokens++;
            
            if (i == n || charToIndex[pattern[i]] != wordToIndex[token])
                return false;
            
            charToIndex[pattern[i]] = wordToIndex[token] = i+1; 
            /*
                Why i+1 ?
                Because by default, if the key is not in map, it's value is returned as 0
                Dry-run this :
                "abba"
                "dog cat cat fish"
            */
            
            i++;
        }
        
        if(countTokens != pattern.size() || i != n)
            return false;
        
        return true;
    }};