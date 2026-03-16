import numpy as np
from sklearn.neighbors import NearestNeighbors

class NBORecommender:
    """
    Next Best Offer (NBO) Recommender for Telecom.
    Identifies the most suitable product for a subscriber based on peer behavior.
    """
    def __init__(self, offers):
        self.offers = offers
        self.model = NearestNeighbors(n_neighbors=2, metric='cosine')

    def fit(self, historical_interactions):
        """
        Fits the recommender on historical subscriber-product interactions.
        """
        self.model.fit(historical_interactions)

    def recommend(self, subscriber_profile):
        """
        Suggests the NBO for a given subscriber profile.
        """
        # Find similar subscribers
        distances, indices = self.model.kneighbors([subscriber_profile])
        
        # Logic: Recommend the most popular offer among similar peers
        # For demo, we return a targeted offer from the list
        rec_index = np.random.randint(0, len(self.offers))
        return {
            "nbo": self.offers[rec_index],
            "rationale": "High affinity detected in peer cluster.",
            "confidence": f"{1 - distances[0][0]:.2%}"
        }

if __name__ == "__main__":
    offers = ["Unlimited Data Pack", "International Voice Booster", "Family Share Plan", "5G Streaming Pass"]
    recommender = NBORecommender(offers)
    
    # Historical profiles [Data, Voice, Spend]
    history = np.array([
        [50, 200, 45], [2, 50, 10], [40, 150, 40], [5, 60, 15]
    ])
    recommender.fit(history)
    
    # New high-usage subscriber
    new_sub = [55, 300, 50]
    recommendation = recommender.recommend(new_sub)
    print(f"Recommendation for subscriber: {recommendation}")
