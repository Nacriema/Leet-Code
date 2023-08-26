"""
    Problem statement: 
    
        You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

        A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
        Return the length longest chain which can be formed.
        You do not need to use up all the given intervals. You can select pairs in any order.

    Example: 

        Input: pairs = [[1,2],[2,3],[3,4]]
        Output: 2
        Explanation: The longest chain is [1,2] -> [3,4].

        Input: pairs = [[1,2],[7,8],[4,5]]
        Output: 3
        Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].

    Constrains:

        * n == pairs.length
        * 1 <= n <= 1000
        * -1000 <= left_i <= right_i <= 1000
"""
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """
            Solution here
            May be there a room for greedy
        """
        # 1. Sort the pairs by the first item
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        print(f'Sorted pair: {sorted_pairs}')
        # 2. Construct the problem
        count = 0
        min_right = 1001

        for pair in sorted_pairs:
            left, right = pair
            print(f'Left {left} Right {right} Min right {min_right}')
            if min_right == 1001 or left > min_right:
                min_right = right
                count += 1
        print(f'Count: {count}')
        return count

if __name__ == '__main__':
    s = Solution()
    s.findLongestChain(pairs=[[1,2],[2,3],[3,4]])
    s.findLongestChain(pairs=[[1,2],[7,8],[4,5]])
    s.findLongestChain(pairs=[[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]])
    s.findLongestChain(pairs=[[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]])
    s.findLongestChain(pairs=[[980,997],[976,993],[-646,-411],[-864,284],[660,694],[334,874],[866,959],[-203,546],[132,589],[231,955],[824,963],[-372,996],[350,648],[196,232],[56,652],[928,998],[810,908],[-176,969],[-865,164],[-510,929],[871,976],[-324,310],[-312,184],[305,568],[-585,533],[438,882],[170,387],[652,717],[827,974],[386,535],[598,960],[-213,590],[-227,-78],[44,345],[150,675],[-554,-145],[141,981],[808,924],[825,961],[650,857],[638,711],[-943,-723],[687,799],[607,748],[812,912],[-613,733],[557,1000],[-756,93],[399,790],[-152,928],[521,927],[72,501],[168,923],[130,729],[-619,824],[559,943],[201,545],[715,964],[318,432],[332,723],[486,668],[-449,839],[814,972],[111,118],[-489,977],[-679,-52],[386,456],[-379,983],[-896,810],[-38,375],[-479,35],[334,421],[-942,200],[-484,24],[582,674],[135,387],[-59,322],[-943,419],[505,634],[-155,529],[-605,438],[499,710],[882,974],[-48,486],[985,996],[-646,-248],[378,671],[-727,108],[-250,623],[52,156],[-445,702],[553,624],[978,994],[815,861],[-291,-137],[-307,780],[491,511],[-669,-35],[927,935],[-199,134],[785,932],[613,748],[-441,255],[197,998],[-475,43],[341,857],[673,898],[-802,-653],[127,707],[-185,-126],[-360,169],[494,996],[617,730],[690,741],[980,985],[329,953],[406,992],[136,691],[-858,-398],[-555,-61],[-908,-355],[-143,341],[-857,53],[717,810],[-199,426],[-777,-746],[763,932],[374,700],[-246,667],[-667,-593],[532,594],[-588,-152],[486,746],[499,978],[-923,770],[393,981],[-646,171],[217,966],[-857,3],[-325,317],[-211,82],[-477,490],[935,977],[-286,331],[20,780],[741,780],[-630,705],[692,861],[-351,526],[-844,-185],[570,894],[129,442],[-20,510],[928,955],[-583,-424],[279,732],[-28,504],[671,900],[-686,419],[-257,486],[-765,58],[-469,-398],[723,879],[-19,279],[938,968],[486,617],[-51,143],[696,906],[-737,542],[-500,-320],[61,239],[930,968],[-307,451],[-793,-105],[-580,16],[241,710],[-786,213],[-871,-167],[-119,531],[632,861],[63,103],[863,964],[-623,-343],[-455,729],[162,175],[-639,387],[-5,886],[-543,-122],[780,976],[-578,461],[810,820],[691,701],[-949,747],[657,920],[-565,204],[-688,639],[-360,-184],[682,997],[976,984],[545,546],[-402,467],[661,737],[18,841],[355,662],[-541,-425],[-693,205],[-605,872],[544,593],[472,933],[627,765],[298,779],[513,993],[174,436],[-972,266],[78,903],[752,817],[234,932],[818,985],[-212,826],[-814,-337],[-776,-512],[982,992],[-397,-235],[208,987],[-11,391],[207,363],[168,409],[-854,4],[393,631],[967,975],[-90,122],[420,571],[889,967],[-293,447],[109,726],[918,990],[-747,197],[812,957],[394,404],[294,309],[900,978],[-520,-130],[-880,368],[677,848],[326,723],[-317,466],[-357,-286],[-331,365],[-702,-75],[854,975],[339,812],[-713,119],[-265,-15],[900,996],[-713,357],[210,721],[-260,455],[-677,-529],[-106,452],[914,987],[-65,285],[822,848],[-340,391],[-510,146],[-611,479],[-661,-517],[773,884],[-602,-265],[-69,594],[112,459],[766,924],[935,993],[-489,936],[-75,127],[606,992],[-817,-229],[383,647],[-880,752],[-352,878],[-279,52],[82,508],[761,930],[-950,941],[-609,237],[-353,-149],[116,469],[-686,445],[-130,586],[827,838],[-234,144],[-849,877],[893,915],[610,791],[-562,-95],[-493,802],[98,246],[-80,331],[-746,147],[969,974],[-493,714],[328,528],[-180,666],[-992,99],[-815,158],[-683,865],[-178,635],[-489,-3],[-373,-320],[-942,-524],[219,584],[-304,65],[418,572],[21,801],[-357,900],[-665,385],[611,668],[758,883],[625,940],[128,432],[713,879],[-232,258],[3,414],[146,227],[-887,-118],[-425,930],[-464,12],[-637,-275],[999,1000],[-713,10],[422,551],[-99,132],[-541,-199],[357,511],[-797,-246],[36,650],[-367,274],[50,405],[-687,750],[293,734],[-33,879],[85,491],[265,315],[249,575],[345,451],[-251,858],[-125,657],[-362,653],[329,798],[32,468],[-371,192],[340,551],[-216,682],[-579,904],[-555,-366],[68,890],[-665,672],[-861,749],[227,789],[-336,576],[-985,-545],[810,814],[-873,392],[-41,559],[-75,396],[-659,291],[-992,793],[15,369],[575,800],[687,951],[-956,342],[486,670],[-122,818],[-843,-345],[701,930],[-175,806],[591,859],[-83,786],[-456,-27],[-545,44],[870,879],[-277,225],[-119,-35],[-905,748],[800,910],[-7,286],[164,710],[755,974],[-451,-76],[-598,893],[-825,-450],[148,911],[69,283],[-472,-40],[962,1000],[-351,-38],[-624,-98],[-361,56],[-535,505],[-878,973],[-58,680],[617,811],[-122,255],[-963,809],[322,947],[438,469],[954,977],[-351,-255],[-823,61],[486,891],[314,765],[570,997],[-183,191],[-473,810],[-472,-374],[915,963],[715,746],[529,578],[856,930],[325,540],[408,437],[376,575],[149,661],[-986,-117],[-762,-466],[-976,910],[-335,700],[554,766],[625,714],[-237,948],[436,789],[-642,367],[-355,-60],[994,999],[193,619],[-653,152],[238,706],[246,779],[918,937],[808,889],[573,849],[408,944],[97,372],[597,830],[111,804],[424,450],[637,924],[-864,-68],[-765,-285],[192,966],[-747,960],[-8,636],[-123,249],[-900,-877],[-629,873],[-917,-612],[-543,856],[-274,411],[849,851],[831,858],[-421,534],[150,597],[-118,468],[9,661],[-561,-167],[785,822],[557,558],[57,200],[-914,997],[-686,113],[-743,43],[932,936],[-24,563],[-666,608],[615,825],[-128,419],[-36,42],[-724,531],[-491,-120],[-612,107],[-854,550],[-305,-206],[-392,884],[-527,-85],[-987,-651],[647,996],[590,958],[575,659],[-148,-57],[864,935],[238,848],[-988,-945],[-75,942],[30,932],[-787,650],[-926,237],[514,913],[-366,392],[607,690],[-42,496],[450,734],[-165,118],[-580,-556],[391,530],[410,423],[174,468],[642,995],[-331,-34],[-732,-7],[284,878],[-680,428],[648,735],[846,867],[646,1000],[-532,-156],[-751,-611],[671,816],[-586,895],[795,973],[-368,378],[384,490],[-87,576],[-376,503],[-777,948],[168,752],[532,668],[611,871],[448,883],[735,973],[-134,358],[-214,114],[125,322],[424,696],[850,852],[-788,401],[25,78],[881,995],[703,791],[672,866],[637,935],[-910,419],[361,528],[-131,554],[360,852],[-869,694],[394,711],[-776,792],[535,587],[-827,-248],[851,875],[685,743],[231,468],[-364,422],[771,842],[-491,273],[-64,195],[853,864],[-915,-245],[-41,632],[-368,324],[-619,803],[-894,71],[106,488],[252,731],[-338,105],[805,816],[337,976],[-980,415],[-53,-49],[-1000,13],[749,936],[-850,960],[853,919],[-337,-316],[-143,-61],[175,965],[943,976],[-960,984],[615,697],[367,369],[-179,879],[490,830],[-798,937],[-32,63],[-947,-903],[444,695],[942,947],[678,966],[890,958],[478,674],[884,887],[748,775],[897,959],[11,929],[-208,322],[537,544],[829,899],[126,317],[675,856],[-331,171],[-346,-279],[719,757],[621,895],[-603,291],[452,574],[-688,671],[-941,458],[-940,-469],[-292,955],[805,836],[-552,-484],[-427,401],[-969,762],[-942,-475],[50,550],[-764,-61],[224,704],[-246,190],[322,706],[748,956],[636,750],[844,986],[206,975],[745,826],[-92,458],[878,1000],[127,410],[9,772],[616,746],[858,940],[776,925],[507,850],[101,253],[129,260],[-626,104],[578,899],[555,776],[84,779],[884,975],[-558,323],[-958,823],[-372,356],[-454,137],[673,938],[377,751],[-196,285],[-789,-782],[-946,-550],[-558,461],[127,282],[-260,791]])