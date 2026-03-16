import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

class MicroSegmentationEngine:
    """
    Micro-segmentation Engine for Telecom Subscriber Personalization.
    Utilizes K-Means clustering to move beyond mass marketing.
    """
    def __init__(self, n_segments=5):
        self.n_segments = n_segments
        self.scaler = StandardScaler()
        self.model = KMeans(n_clusters=n_segments, random_state=42, n_init=10)

    def process_data(self, data):
        """
        Scales and fits the subscriber data for micro-segmentation.
        """
        scaled_data = self.scaler.fit_transform(data)
        self.model.fit(scaled_data)
        return self.model.labels_

    def get_segment_summary(self, data, labels):
        """
        Provides a profile for each micro-segment.
        """
        data['segment'] = labels
        summary = data.groupby('segment').mean()
        return summary

if __name__ == "__main__":
    # Mock industrial data: [Data Usage (GB), Voice Usage (min), ARPU (USD)]
    X = np.array([
        [1.2, 50, 10], [45.0, 300, 60], [15.0, 100, 35],
        [0.5, 20, 8], [60.0, 500, 75], [10.0, 80, 30]
    ])
    df = pd.DataFrame(X, columns=['data_usage', 'voice_usage', 'arpu'])
    
    engine = MicroSegmentationEngine(n_segments=2)
    labels = engine.process_data(df)
    print(f"Subscriber Labels: {labels}")
    print(f"Segment Profiles:\n{engine.get_segment_summary(df, labels)}")
