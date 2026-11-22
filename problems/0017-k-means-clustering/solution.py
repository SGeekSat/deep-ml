import numpy as np
def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
   

    points = np.array(points, dtype=float)
    centroids = np.array(initial_centroids, dtype=float)

    for _ in range(max_iterations):

        # Step 1: Calculate distance of every point from every centroid
        distances = np.linalg.norm(
            points[:, np.newaxis, :] - centroids[np.newaxis, :, :],
            axis=2
        )

        # Step 2: Assign each point to its nearest centroid
        labels = np.argmin(distances, axis=1)

        # Step 3: Update centroids
        new_centroids = []

        for i in range(k):
            cluster_points = points[labels == i]

            if len(cluster_points) > 0:
                new_centroids.append(np.mean(cluster_points, axis=0))
            else:
                new_centroids.append(centroids[i])

        new_centroids = np.array(new_centroids)

        # Step 4: Check convergence
        if np.allclose(centroids, new_centroids):
            centroids = new_centroids
            break

        centroids = new_centroids
    return [tuple(np.round(c, 4)) for c in centroids]

    