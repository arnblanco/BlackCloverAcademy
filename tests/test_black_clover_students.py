import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from sqlalchemy.ext.asyncio import AsyncSession
from server import app, get_db_session

client = TestClient(app)

# Datos de prueba
student_data = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "identificacion": "ABC12345",
    "edad": 18,
    "afinidad_magica": "Fuego",
}

@pytest.fixture(scope="module")
def test_app():
    with TestClient(app, backend="asyncio") as test_client:
        yield test_client

@pytest.fixture
async def mock_db_session():
    async with AsyncMock(AsyncSession) as mock_session:
        yield mock_session

@pytest.fixture
def anyio_backend():
    return 'asyncio'

@pytest.mark.anyio
async def test_index(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome to FastApi starter project!!"}

@pytest.mark.anyio
async def test_get_students_list(test_app, mock_db_session):
    with patch("server.get_db_session", return_value=mock_db_session):
        response = test_app.get("/solicitud")
        assert response.status_code == 200

@pytest.mark.anyio
async def test_create_student(test_app, mock_db_session):
    with patch("server.get_db_session", return_value=mock_db_session):
        data = {
            "nombre": "Juan",
            "apellido": "Pérez",
            "identificacion": "ABC12345",
            "edad": 18,
            "afinidad_magica": "Fuego"
        }
        response = test_app.post("/solicitud", json=data)
        assert response.status_code == 200
        response_data = response.json()
        
        assert response_data["nombre"] == data['nombre']
        assert response_data["apellido"] == data['apellido']
        assert response_data["identificacion"] == data['identificacion']
        assert response_data["edad"] == data['edad']
        assert response_data["afinidad_magica"] == data['afinidad_magica']
        assert "id" in response_data

@pytest.mark.anyio
async def test_update_student(test_app, mock_db_session):
    with patch("server.get_db_session", return_value=mock_db_session):
        data = {
            "nombre": "Carlos",
            "apellido": "Sánchez",
        }
        response = test_app.put("/solicitud/1", json=data)
        assert response.status_code == 200
        response_data = response.json()

        assert response_data["nombre"] == data['nombre']
        assert response_data["apellido"] == data['apellido']

@pytest.mark.anyio
async def test_update_student_status(test_app, mock_db_session):
    with patch("server.get_db_session", return_value=mock_db_session):
        response = test_app.patch("/solicitud/1")
        assert response.status_code == 200
        response_data = response.json()

@pytest.mark.anyio
async def test_delete_student(test_app, mock_db_session):
    with patch("server.get_db_session", return_value=mock_db_session):
        response = test_app.delete("/solicitud/1")
        assert response.status_code == 200
        assert response.json() is True

@pytest.mark.anyio
async def test_get_full_list(test_app, mock_db_session):
    with patch("server.get_db_session", return_value=mock_db_session):
        response = test_app.get("/asignaciones")
        assert response.status_code == 200
