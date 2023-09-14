"""
    Problem Statement:
        You are given a list of airline tickets where ticket[i] = [from_i, to_i] represent the departrue and 
        the arrival airpots of the flight. Reconstruct the itnitararay on order and return it.
        
        All of the tickets belong to a main who dparts from "JFK" thus, the intinararay must begin with "JFK". 
        If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical 
        order when read as a single string.
        
        For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"]s
        
        You may assume all tikets from at least one valid itinerary. You must use all the tickets once and only once.
        
    Example 1:
        Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
        Output: ["JFK","MUC","LHR","SFO","SJC"]
        
    Example 2:
        Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
        Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
        Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

    Constrains:
        * 1 <= tickets.length <= 300
        * tickets[i].length == 2
        * from_i.length == 3
        * to_i.length == 3
        * from_i and to_i consist uppercase English letters.
        * from_i != to_i
"""
from typing import List


class Solution:
    # TLE Solution
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
            Any ideas: 
                * Start of the chains is "JFK"
                * Must use all the tickets, each ticket use once and only once
            
            => Exact cover problems ??? The puzzles is the tickets array, then we try to use all of our puzzles to complete 
            the picture.
            
            Get all possible solutions, and then use the comparision filter to return the smallest lexical order. 
            
            
            First, I use backtracking wit memorization for each state   
                - Form the dictionary in memory like this [{"current_itinerary": ..., "remain_tiket": ...}]
                - The stop condition is the empty of memory
                - Inside the while loop, I also add some sort of stop criteria to prune not good solution

            TODO: Oprimize this code
        """    
        def convert(tks):
            rs = [x[0] for x in tks]
            rs.append(tks[-1][1])
            return rs
                
        memo = []
        itineraries = []
        
        # Sort the tickets array by lexico order of the start departure 
        tickets = sorted(tickets, key=lambda x: (x[1]), reverse=True)
        
        print(f'Tickets sorted: {tickets}')
        
        
        # 1. Prepare for the first tiket, start is always "JFK" and sort by the last item to be more lexico
        init_ticket = list(filter(lambda x: x[0] == "JFK", tickets))
        
        print(f'Init tickets: {init_ticket}')
        
        for i, ticket in enumerate(tickets):
            if ticket in init_ticket:
                memo.append(([ticket], tickets[:i] + tickets[i+1:]))
        
        print(f'Memo: {memo}')
        
        # 2. Main process
        while len(memo):
            # Loop through the memo, preprocess it and then 
            latest_itinerary, remain_tickets = memo.pop()
            
            # If the length of remain tickets is 0, mean we have the result 
            if len(remain_tickets) == 0: 
                itineraries.append(latest_itinerary)
                print(f'Latest: {latest_itinerary}')
                # At this time, we have the solution, so we dont need to do more
                break
                
            last_node = latest_itinerary[-1]
            
            # Loop through the remain tickets, find which start name like the last node, if matched then append this into the memo for the next search
            for i, ticket in enumerate(remain_tickets):
                if ticket[0] == last_node[1]:
                    # Found a new one, then add them into the memo candidate
                    memo.append((latest_itinerary + [ticket], remain_tickets[:i] + remain_tickets[i + 1:]))
        
        # 3. Final processing ...
        print(f'Finally: {itineraries}')

        itineraries = list(map(convert, itineraries))
        return itineraries[0]    
    
s = Solution()
# print(s.findItinerary(tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
# print(s.findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(s.findItinerary(tickets = [["AXA","EZE"],["EZE","AUA"],["ADL","JFK"],["ADL","TIA"],["AUA","AXA"],["EZE","TIA"],["EZE","TIA"],["AXA","EZE"],["EZE","ADL"],["ANU","EZE"],["TIA","EZE"],["JFK","ADL"],["AUA","JFK"],["JFK","EZE"],["EZE","ANU"],["ADL","AUA"],["ANU","AXA"],["AXA","ADL"],["AUA","JFK"],["EZE","ADL"],["ANU","TIA"],["AUA","JFK"],["TIA","JFK"],["EZE","AUA"],["AXA","EZE"],["AUA","ANU"],["ADL","AXA"],["EZE","ADL"],["AUA","ANU"],["AXA","EZE"],["TIA","AUA"],["AXA","EZE"],["AUA","SYD"],["ADL","JFK"],["EZE","AUA"],["ADL","ANU"],["AUA","TIA"],["ADL","EZE"],["TIA","JFK"],["AXA","ANU"],["JFK","AXA"],["JFK","ADL"],["ADL","EZE"],["AXA","TIA"],["JFK","AUA"],["ADL","EZE"],["JFK","ADL"],["ADL","AXA"],["TIA","AUA"],["AXA","JFK"],["ADL","AUA"],["TIA","JFK"],["JFK","ADL"],["JFK","ADL"],["ANU","AXA"],["TIA","AXA"],["EZE","JFK"],["EZE","AXA"],["ADL","TIA"],["JFK","AUA"],["TIA","EZE"],["EZE","ADL"],["JFK","ANU"],["TIA","AUA"],["EZE","ADL"],["ADL","JFK"],["ANU","AXA"],["AUA","AXA"],["ANU","EZE"],["ADL","AXA"],["ANU","AXA"],["TIA","ADL"],["JFK","ADL"],["JFK","TIA"],["AUA","ADL"],["AUA","TIA"],["TIA","JFK"],["EZE","JFK"],["AUA","ADL"],["ADL","AUA"],["EZE","ANU"],["ADL","ANU"],["AUA","AXA"],["AXA","TIA"],["AXA","TIA"],["ADL","AXA"],["EZE","AXA"],["AXA","JFK"],["JFK","AUA"],["ANU","ADL"],["AXA","TIA"],["ANU","AUA"],["JFK","EZE"],["AXA","ADL"],["TIA","EZE"],["JFK","AXA"],["AXA","ADL"],["EZE","AUA"],["AXA","ANU"],["ADL","EZE"],["AUA","EZE"]]))

