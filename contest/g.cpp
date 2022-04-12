#include <iostream>
#include <vector>
#include <cmath>


struct point {

    int x;
    int y;

};

using namespace std;


int distances[1000][1000];
int path[1000][1000];
const int MAX_DIST = 1001;



int dist(point p1, point p2) {

    return abs(p1.x - p2.x) + abs(p1.y - p2.y);

}


int find_path(int start, int dest, int k, std::vector<int>& cities) {

    if (path[start][dest] != -1)
        return path[start][dest];

    int min_len = MAX_DIST + 1;
    for (int c = 0; c < cities.size(); ++c) {

        if (cities[c] && distances[start][c] <= k) {

            cities[c] = 0;
            int new_path = find_path(c, dest,  k, cities) + 1;
            cities[c] = 1;

            if (new_path <= min_len)
                min_len = new_path;

        }

    }


    path[start][dest] = min_len;
    return path[start][dest];

}


int main() {

    int n;
    cin >> n;
    std::vector<point> city(n);
    std::vector<int> cities(n, 1);
    int x, y;
    point p;
    for (int i = 0; i < n; ++i) {
        cin >> x;
        cin >> y;
        point p;
        p.x = x;
        p.y = y;
        city[i] = p;
    }

    for (int i = 0; i < n; ++i) {

        for (int j = 0; j < n; ++j) {

            distances[i][j] = dist(city[i], city[j]);
            path[i][j] = -1;
            if (i == j) {
                path[i][j] = 0;
            }

        }

    }

    int k;
    cin >> k;
    int start, dest;
    cin >> start >> dest;
    start -= 1;
    dest -= 1;

    cities[start] = 1;


    int minpath  = find_path(start, dest, k, cities);


    if (minpath >= MAX_DIST)
        minpath = -1;

    cout << minpath;


}
