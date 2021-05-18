from sklearn.neighbors import NearestNeighbors
import numpy as np

class Rcomendaror:
    def __init__(self, n, mutation):
        self.audio = []
        self.video = []
        self.article = []
        self.n_neighbors = n;
        self.mutation_rate = mutation

    def get_nearest(self, user, other_users):

        user_data = np.array(user)
        other_data = np.array(other_users)

        if user_data.shape[0] == 0 or other_data.shape[0] == 0 :
            self.nearest = 0
            return
        neighbors = NearestNeighbors(n_neighbors=self.n_neighbors+1)
        neighbors.fit(other_data)
        self.nearest = neighbors.kneighbors([user_data],n_neighbors+1, return_distance=False)[0][1] + 1
        return self.nearest

    def fill_recomendatioms(self, view, general, recomedations):
        i = 0
        view_s = len(set(view))
        while i < 3 and len(recomedations) < len(general):
            mutation = np.random.rand()
            if mutation > self.mutation_rate and len(recomedations) < view_s:
                index = np.random.randint(0, len(view))
                if not view[index] in recomedations:
                    recomedations.append(view[index])
                    i+= 1
            else:
                index = np.random.randint(0, len(general))
                if not general[index] in recomedations:
                    recomedations.append(general[index])
                    i += 1

    def generate_recomendations(self, audio, video, article, audioV, videoV, articleV):
        selfaudio = self.audio
        selfvideo = self.video
        selfarticle = self.article
        self.fill_recomendatioms(audioV, audio, selfaudio)
        self.fill_recomendatioms(videoV, video, selfvideo)
        self.fill_recomendatioms(articleV, article, selfarticle)
        self.audio = selfaudio
        self.video = selfvideo
        self.article = selfarticle
        return self.audio , self.video , self.article








