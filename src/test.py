import pytest
import os
from dotenv import dotenv_values
from service import CLUService


class TestCLuService:

    @pytest.fixture
    def clu_service(self):
        env_path = os.path.join(os.path.dirname(__file__), "../.env") 
        env_vars = dotenv_values(env_path)
        API_KEY = env_vars["API_KEY"]
        ENDPOINT = "https://dataleont.cognitiveservices.azure.com/language/:analyze-conversations?api-version=2022-10-01-preview"
        return CLUService(API_KEY, ENDPOINT)
    
    
    def test_get_recipe(self, clu_service):
        query = "I want to make nems. Can you share a recipe?"
        response = clu_service.get_intent(query)
        assert response == "GetRecipe"

    def test_get_ingredients(self, clu_service):
        query = "Can you tell me the ingredients for ham sandwich?"
        response = clu_service.get_intent(query)
        assert response == "GetIngredient"
            
    def test_get_recipe2(self, clu_service):
        query = "I want to make chicken. Can you share a recipe?"
        response = clu_service.get_intent(query)
        assert response == "GetRecipe"
            
    def test_get_ingredients2(self, clu_service):
        query = "Can you tell me the ingredients for cheesecake?"
        response = clu_service.get_intent(query)
        assert response == "GetIngredient"
            
    def test_get_recipe3(self, clu_service):
        query = "I want to make chocolate cake. Can you share a recipe?"
        response = clu_service.get_intent(query)
        assert response == "GetRecipe"
            
    def test_get_ingredients3(self, clu_service):
        query = "Can you tell me the ingredients for pizza?"
        response = clu_service.get_intent(query)
        assert response == "GetIngredient"
                
    def test_get_recipe4(self, clu_service):
        query = "I want to make pasta. Can you share a recipe?"
        response = clu_service.get_intent(query)
        assert response == "GetRecipe"
                
    def test_get_ingredients4(self, clu_service):
        query = "Can you tell me the ingredients for sushi?"
        response = clu_service.get_intent(query)
        assert response == "GetIngredient"
            
    def test_get_recipe5(self, clu_service):
        query = "I want to make a cake. Can you share a recipe?"
        response = clu_service.get_intent(query)
        assert response == "GetRecipe"
                
    def test_get_ingredients5(self, clu_service):
        query = "Can you tell me the ingredients for a ice tea?"
        response = clu_service.get_intent(query)
        assert response == "GetIngredient"
                
   
    
    