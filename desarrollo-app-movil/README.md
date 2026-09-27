# Desarrollo App Móvil Android — Tracker de Entrenamiento y Nutrición

## Descripción del Proyecto

Aplicación Android nativa para la gestión de rutinas de entrenamiento de fuerza (4-5 días por semana) y control estricto de macronutrientes.

## Metodología

**Mobile-D** — Ciclo iterativo de 5 fases:
1. **Exploration** — Análisis y diseño inicial
2. **Initialization** — Configuración del proyecto
3. **Development** — Implementación de features
4. **Stabilization** — Testing, integración, QA
5. **System Release** — Entrega y deployment

## Sprint 1 — Tracker + Calorías

Enfoque en dos pilares fundamentales:

### 📊 Tracker de Entrenamiento
- Crear y gestionar rutinas de fuerza personalizadas
- Registrar sesiones diarias (series, reps, peso)
- Visualizar progreso y volumen total

### 🍎 Control de Calorías y Macros
- Base de datos de alimentos embebida
- Cálculo automático de ingesta diaria
- Dashboard de adherencia nutricional

## Estructura del Proyecto

```
desarrollo-app-movil/
├── .github/
│   └── workflows/
│       └── mobile-d-stabilize.yml    # Pipeline CI/CD Stabilize
├── docs/
│   └── SPRINT_1_BACKLOG.md          # Historias de usuario + DoD
├── app/
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/
│   │   │   │   └── com/trainingapp/
│   │   │   │       ├── ui/
│   │   │   │       ├── viewmodel/
│   │   │   │       ├── db/
│   │   │   │       ├── model/
│   │   │   │       └── utils/
│   │   │   ├── res/
│   │   │   └── AndroidManifest.xml
│   │   └── test/
│   ├── build.gradle
│   └── proguard-rules.pro
├── build.gradle
├── settings.gradle
└── README.md
```

## Historias de Usuario - Sprint 1

Ver detalles completos en: [`docs/SPRINT_1_BACKLOG.md`](docs/SPRINT_1_BACKLOG.md)

1. **HU-001:** Registro e inicio de sesión (13 pts)
2. **HU-002:** Crear rutina de entrenamiento (13 pts)
3. **HU-003:** Registrar sesión diaria (8 pts)
4. **HU-004:** Cálculo de calorías/macros (13 pts)
5. **HU-005:** Dashboard de progreso (8 pts)

**Total Sprint 1:** 55 puntos

## Pipeline CI/CD — Fase Stabilize

El workflow `.github/workflows/mobile-d-stabilize.yml` ejecuta en cada push a `main`:

✅ Setup Java 17  
✅ Ejecutar tests unitarios (`./gradlew test`)  
✅ Compilar APK Debug (`./gradlew assembleDebug`)  
✅ Generar cobertura (Jacoco)  
✅ Análisis estático (Lint)  
✅ Subir artefactos (APK + reports)  

## Tecnologías

### Backend Local
- **Room Database** — ORM local SQLite
- **LiveData** — Observables reactivos
- **ViewModel** — Gestión de estado

### UI
- **Fragment Architecture** — Modular y escalable
- **RecyclerView** — Listas optimizadas
- **Material Design 3** — Componentes modernos

### Datos
- **Firebase Authentication** (opcional)
- **Embedded SQLite** para base de alimentos
- **SharedPreferences / DataStore** para sesiones

### Testing
- **JUnit 4** — Tests unitarios
- **Mockito** — Mocking de dependencias
- **Espresso** — Tests de UI
- **Jacoco** — Cobertura de código

## Cómo Comenzar

### Requisitos
- Android Studio 2022.1+
- JDK 17+
- Gradle 8.0+
- Android API 28+

### Instalación

```bash
# Clonar repositorio
git clone https://github.com/i22lumas/Proyectos.git
cd desarrollo-app-movil

# Crear proyecto Android Studio
# Importar en Android Studio como Gradle project

# Compilar
./gradlew build

# Ejecutar tests
./gradlew test

# Instalar en emulador/dispositivo
./gradlew installDebug
```

## Control de Versiones

- **main** — Rama estable (solo PRs verificadas)
- **develop** — Rama de desarrollo
- **feature/** — Features del sprint
- **hotfix/** — Bugs críticos

## Contribución

1. Crear rama: `git checkout -b feature/HU-XXX-descripcion`
2. Hacer cambios y commits
3. Push y crear Pull Request
4. CI/CD valida automáticamente
5. Code review y merge a `develop`
6. Merge a `main` al finalizar sprint

## Roadmap

- **Sprint 1** (Actual): Tracker + Calorías básico
- **Sprint 2**: Gráficos, historial, estadísticas
- **Sprint 3**: Sincronización cloud, social features
- **Sprint 4+**: IA/recomendaciones, wearables

## Contacto

**Product Owner & DevOps:** [i22lumas](https://github.com/i22lumas)  
**Repositorio:** https://github.com/i22lumas/Proyectos/tree/main/desarrollo-app-movil

---

*Última actualización: Septiembre 2026*
