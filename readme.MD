## Machine Learning deployment

- Find a trained machine learning model
    - #Copy paste network
    - Load weights externally, not fixed to be able to update model.
- Make it available through an API (fastAPI)
    - FastAPI
- Containarize with docker
    - Make a Dockerfile
    - 
- Deploy to a docker cloud host (cloud run?)


https://paperswithcode.com/paper/old-photo-restoration-via-deep-latent-space


Det här kan vara ett kul projekt. Se om vi kan paketera ihop den här AI-modellen som finns med kod och erbjuda den genom ett API.

Steg som kan vara roliga att pröva.

1. Bygga en web-app där du kan pröva att skicka in en bild och få ett svar i form av en retoucherad bild.
2. Bygga ett backend-api som hanterar bilderna som skickas in.
3. Spara en tränad AI-modell och använd den för att förändra bilderna.
4. Deploya det här med tex Docker + Kubernetes på AWS eller Google Cloud eller Digital Ocean eller vad som kan vara roligt 