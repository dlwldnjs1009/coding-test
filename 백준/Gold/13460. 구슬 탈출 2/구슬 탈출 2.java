import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static char[][] board;
    static int[] dx = {-1, 1, 0, 0};  // 상하좌우
    static int[] dy = {0, 0, -1, 1};
    
    static class State {
        int rx, ry, bx, by, count;
        
        State(int rx, int ry, int bx, int by, int count) {
            this.rx = rx;
            this.ry = ry;
            this.bx = bx;
            this.by = by;
            this.count = count;
        }
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new char[N][M];
        
        int rx = 0, ry = 0, bx = 0, by = 0;
        
        // 보드 입력 및 구슬 위치 찾기
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                board[i][j] = line.charAt(j);
                if (board[i][j] == 'R') {
                    rx = i; ry = j;
                    board[i][j] = '.';  // 빈 칸으로 변경
                } else if (board[i][j] == 'B') {
                    bx = i; by = j;
                    board[i][j] = '.';  // 빈 칸으로 변경
                }
            }
        }
        
        System.out.println(bfs(rx, ry, bx, by));
    }
    
    static int bfs(int rx, int ry, int bx, int by) {
        Queue<State> queue = new LinkedList<>();
        // 방문 체크: 4차원 배열 (빨간구슬x, 빨간구슬y, 파란구슬x, 파란구슬y)
        boolean[][][][] visited = new boolean[N][M][N][M];
        
        queue.offer(new State(rx, ry, bx, by, 0));
        visited[rx][ry][bx][by] = true;
        
        while (!queue.isEmpty()) {
            State current = queue.poll();
            
            // 10번 초과시 실패
            if (current.count >= 10) {
                return -1;
            }
            
            // 4방향 기울이기
            for (int dir = 0; dir < 4; dir++) {
                int nrx = current.rx;
                int nry = current.ry;
                int nbx = current.bx;
                int nby = current.by;
                
                // 빨간 구슬 이동
                boolean redHole = false;
                while (board[nrx + dx[dir]][nry + dy[dir]] != '#') {
                    nrx += dx[dir];
                    nry += dy[dir];
                    if (board[nrx][nry] == 'O') {
                        redHole = true;
                        break;
                    }
                }
                
                // 파란 구슬 이동
                boolean blueHole = false;
                while (board[nbx + dx[dir]][nby + dy[dir]] != '#') {
                    nbx += dx[dir];
                    nby += dy[dir];
                    if (board[nbx][nby] == 'O') {
                        blueHole = true;
                        break;
                    }
                }
                
                // 파란 구슬이 구멍에 빠지면 실패
                if (blueHole) {
                    continue;
                }
                
                // 빨간 구슬만 구멍에 빠지면 성공
                if (redHole) {
                    return current.count + 1;
                }
                
                // 두 구슬이 같은 위치에 있을 경우 처리
                if (nrx == nbx && nry == nby) {
                    // 더 많이 이동한 구슬을 한 칸 뒤로
                    int redDist = Math.abs(nrx - current.rx) + Math.abs(nry - current.ry);
                    int blueDist = Math.abs(nbx - current.bx) + Math.abs(nby - current.by);
                    
                    if (redDist > blueDist) {
                        nrx -= dx[dir];
                        nry -= dy[dir];
                    } else {
                        nbx -= dx[dir];
                        nby -= dy[dir];
                    }
                }
                
                // 방문하지 않은 상태면 큐에 추가
                if (!visited[nrx][nry][nbx][nby]) {
                    visited[nrx][nry][nbx][nby] = true;
                    queue.offer(new State(nrx, nry, nbx, nby, current.count + 1));
                }
            }
        }
        
        return -1;  // 10번 이내에 못 빼면 -1
    }
}