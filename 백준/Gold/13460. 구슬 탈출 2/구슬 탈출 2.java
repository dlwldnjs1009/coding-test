import java.io.*;
import java.util.*;

public class Main {

    static final int[] dx = {-1, 1, 0, 0};
    static final int[] dy = {0, 0, -1, 1};

    static int N, M;
    static char[][] board;

    static class State {
        int rx, ry, bx, by, depth;
        State(int rx, int ry, int bx, int by, int depth) {
            this.rx = rx; this.ry = ry; this.bx = bx; this.by = by; this.depth = depth;
        }
    }

    static class Roll {
        int x, y, moved;
        boolean inHole;
        Roll(int x, int y, int moved, boolean inHole) {
            this.x = x; this.y = y; this.moved = moved; this.inHole = inHole;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new char[N][M];

        int rx = -1, ry = -1, bx = -1, by = -1;
        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = 0; j < M; j++) {
                char c = s.charAt(j);
                if (c == 'R') { rx = i; ry = j; board[i][j] = '.'; }
                else if (c == 'B') { bx = i; by = j; board[i][j] = '.'; }
                else board[i][j] = c;
            }
        }

        System.out.println(bfs(rx, ry, bx, by));
    }

    static int bfs(int rx, int ry, int bx, int by) {
        boolean[][][][] vis = new boolean[N][M][N][M];
        ArrayDeque<State> q = new ArrayDeque<>();
        q.offer(new State(rx, ry, bx, by, 0));
        vis[rx][ry][bx][by] = true;

        while (!q.isEmpty()) {
            State cur = q.poll();
            if (cur.depth >= 10) continue; // 10회 이내만 확장

            for (int dir = 0; dir < 4; dir++) {
                Roll r = roll(cur.rx, cur.ry, dir);
                Roll b = roll(cur.bx, cur.by, dir);

                if (b.inHole) continue;           // 파랑 빠지면 실패
                if (r.inHole) return cur.depth + 1; // 빨강만 빠지면 성공

                // 같은 칸 충돌 처리: 더 많이 이동한 구슬을 한 칸 뒤로
                if (r.x == b.x && r.y == b.y) {
                    if (r.moved > b.moved) {
                        r.x -= dx[dir]; r.y -= dy[dir];
                    } else {
                        b.x -= dx[dir]; b.y -= dy[dir];
                    }
                }

                if (!vis[r.x][r.y][b.x][b.y]) {
                    vis[r.x][r.y][b.x][b.y] = true;
                    q.offer(new State(r.x, r.y, b.x, b.y, cur.depth + 1));
                }
            }
        }
        return -1;
    }

    static Roll roll(int x, int y, int dir) {
        int nx = x, ny = y, mv = 0;
        while (true) {
            int tx = nx + dx[dir], ty = ny + dy[dir];
            if (board[tx][ty] == '#') break;
            nx = tx; ny = ty; mv++;
            if (board[nx][ny] == 'O') return new Roll(nx, ny, mv, true);
        }
        return new Roll(nx, ny, mv, false);
    }
}
