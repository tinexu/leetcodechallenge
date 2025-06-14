class Solution {
    public void spiral(int[][] matrix, int left, int right, int top, int bottom, List<Integer> res) {
        if ((left > right) || (top > bottom)) {
            return;
        }

        for (int j = left; j <= right; j++) {
            res.add(matrix[top][j]);
        }

        for (int i = top + 1; i <= bottom; i++) {
            res.add(matrix[i][right]);
        }

        if (top < bottom) {
            for (int j = right - 1; j >= left; j--) {
                res.add(matrix[bottom][j]);
            }
        }

        if (left < right) {
            for (int i = bottom - 1; i > top; i--) {
                res.add(matrix[i][left]);
            }
        }

        spiral(matrix, left + 1, right - 1, top + 1, bottom - 1, res);
    }

    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>();

        spiral(matrix, 0, matrix[0].length - 1, 0, matrix.length - 1, res);

        return res;
    }   
}
