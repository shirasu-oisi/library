class SegTree:
    def __init__(self, A, f, e):
        """
        A: セグ木に乗せたい配列
        f: 二項演算 (モノイドじゃなきゃだめ)
        e: f の単位元
        """
        n = len(A)
        c = [e] * (2*n)

        for i in range(N):
            c[i+n] = A[i] # 葉をA[i]の値にする
        
        for i in range(n-1, 0, -1):
            c[i] = f(c[i<<1|0], c[i<<1|1]) # 子を使ってボトムアップに値を更新していく
        
        self.n = n # セグ木の葉の数
        self.c = c # セグ木の配列
        self.e = e
        self.f = f
    
    def update(self, k, x):
        k += self.n
        self.c[k] = x # 対応する葉に移動

        # 祖先をたどって更新していく
        while k > 1:
            k >>= 1
            self.c[k] = self.f(self.c[k<<1|0], self.c[k<<1|1])

    def query(self, l, r):
        res = self.e
        l += self.n; r += self.n # 対応する葉に移動

        while l < r: # 範囲がかぶらない間
            if l & 1: # 左端が右の子なら
                res = self.f(res, self.c[l]) # その値と res の積をとって
                l += 1 # 右に 1 動く

            if r & 1: # 右端が右の子なら
                r -= 1 # 左に 1 動いて
                res = self.f(res, self.c[r]) # その値と res の積をとる

            l >>= 1; r >>= 1 # 親に移動
        
        return res