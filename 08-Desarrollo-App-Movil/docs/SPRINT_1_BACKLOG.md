# Sprint 1 — Backlog de Producto

## Mobile-D: Tracker de Entrenamiento + Control de Calorías

---

# HU-001: Registro e Inicio de Sesión de Usuario

**Descripción:**
Como usuario nuevo, quiero crear una cuenta y autenticarme en la aplicación para acceder a mis rutinas de entrenamiento y datos de nutrición.

**Criterios de Aceptación (DoD):**
- [ ] El usuario puede registrarse con email, contraseña y datos básicos (nombre, edad, peso, altura)
- [ ] La contraseña debe cumplir mínimo 8 caracteres, 1 mayúscula, 1 número
- [ ] El sistema valida que el email no esté registrado previamente
- [ ] Al registrarse, se crea automáticamente el perfil nutricional con macros iniciales (40C/30P/30G)
- [ ] El usuario puede iniciar sesión con email y contraseña
- [ ] La sesión persiste localmente incluso tras cerrar la app (usando SharedPreferences o DataStore)
- [ ] Error handling: mensajes claros para credenciales inválidas o email duplicado

**Tareas Técnicas:**
- [ ] Configurar Firebase Authentication (o implementar backend propio)
- [ ] Diseñar entidad User en Room Database con campos: id, email, nombre, edad, peso, altura, tdee_estimado
- [ ] Crear LoginActivity y RegisterActivity con validaciones en client
- [ ] Implementar SharedPreferences para almacenar token de sesión
- [ ] Crear tests unitarios: validación de email, contraseña y credenciales duplicadas

**Puntos de Historia:** XL (13 puntos)
**Prioridad:** Crítica
**Sprint:** 1

---

# HU-002: Crear y Visualizar Rutina de Entrenamiento

**Descripción:**
Como usuario, quiero crear una rutina de entrenamiento semanal (4-5 días) con ejercicios específicos para cada día, para organizar mi plan de fuerza.

**Criterios de Aceptación (DoD):**
- [ ] El usuario puede crear una nueva rutina asignando nombre (ej: "Push/Pull/Legs")
- [ ] Puede seleccionar 4 o 5 días de la semana para entrenar
- [ ] Para cada día, puede agregar múltiples ejercicios (nombre, series, repeticiones, peso)
- [ ] Cada ejercicio muestra: nombre, series planeadas, reps planeadas, peso
- [ ] El usuario puede editar/eliminar ejercicios de la rutina
- [ ] La rutina se guarda localmente en Room Database
- [ ] Se muestra una vista de lista con todas las rutinas creadas
- [ ] Validación: mínimo 1 ejercicio por día, mínimo 4 días seleccionados

**Tareas Técnicas:**
- [ ] Diseñar entidades Room: Workout, WorkoutDay, Exercise con relaciones
- [ ] Crear WorkoutDAO con CRUD operations
- [ ] Implementar WorkoutViewModel con LiveData
- [ ] Diseñar WorkoutCreationActivity y ExerciseListFragment
- [ ] RecyclerView con adaptador para listar ejercicios por día
- [ ] Persistencia de rutinas en Room
- [ ] Tests unitarios: validación de días/ejercicios, CRUD en Room

**Puntos de Historia:** XL (13 puntos)
**Prioridad:** Crítica
**Sprint:** 1

---

# HU-003: Registrar Sesión de Entrenamiento Diaria

**Descripción:**
Como usuario, quiero registrar el detalle de cada sesión de entrenamiento (series, reps y peso ejecutados) para trackear mi progreso.

**Criterios de Aceptación (DoD):**
- [ ] Al iniciar un día de rutina, puedo ver los ejercicios planeados
- [ ] Para cada ejercicio, puedo registrar: series completadas, reps completadas, peso levantado
- [ ] Diferenciación visual entre planeado vs ejecutado
- [ ] Puedo marcar ejercicio como completado
- [ ] Al completar la sesión, se guarda el registro con timestamp
- [ ] Histórico: puedo ver sesiones pasadas de entrenamiento
- [ ] Cálculo de volumen total: Peso × Series × Reps para cada ejercicio
- [ ] Validación: no permitir reps > 100, peso > 500kg

**Tareas Técnicas:**
- [ ] Diseñar entidad WorkoutSession en Room con relación a Workout
- [ ] Crear entidad ExerciseLog con: ejercicio_id, series, reps, peso, timestamp
- [ ] Implementar SessionDAO con queries para obtener sesión actual
- [ ] Crear TrainingLogFragment con formulario para ingresar datos
- [ ] Mostrar diferencia: planeado vs ejecutado (comparación visual)
- [ ] Cálculo automático de volumen
- [ ] Tests unitarios: cálculo de volumen, validaciones de entrada

**Puntos de Historia:** L (8 puntos)
**Prioridad:** Crítica
**Sprint:** 1

---

# HU-004: Cálculo y Seguimiento Diario de Calorías y Macronutrientes

**Descripción:**
Como usuario, quiero registrar mis comidas y calcular automáticamente las calorías y macronutrientes consumidos diariamente para controlar mi déficit/superávit calórico.

**Criterios de Aceptación (DoD):**
- [ ] El usuario puede buscar alimentos en base de datos (Generada localmente o con API como USDA FoodData Central)
- [ ] Al seleccionar un alimento, ingresa cantidad (en gramos o porciones)
- [ ] Sistema calcula automáticamente: calorías, proteínas, carbohidratos, grasas
- [ ] Muestra meta diaria de calorías basada en: peso × 30 (estimación TDEE básica)
- [ ] Visualización diaria con: calorías totales, macros consumidas vs meta
- [ ] Barra de progreso visual para calorías (0% a 100% o más)
- [ ] Histórico de comidas del día (timestamp, alimento, cantidad, cals)
- [ ] Opción de agregar alimento personalizado con macros manuales
- [ ] Validación: calorías > 0, macros suma no mayor a 10,000 cal

**Tareas Técnicas:**
- [ ] Diseñar entidades Room: Food, FoodLog, DailyNutritionSummary
- [ ] Crear FoodDatabase con ~500 alimentos comunes (SQLite embebido)
- [ ] Implementar NutritionDAO con queries por día
- [ ] Crear NutritionCalculator: clase con métodos estáticos para calcular TDEE, macros
- [ ] Diseñar NutritionTrackerFragment con RecyclerView de comidas
- [ ] Implementar ProgressBar y visualización de macros (Pie chart o stacked bar)
- [ ] Tests unitarios: cálculos de calorías/macros, TDEE estimation

**Puntos de Historia:** XL (13 puntos)
**Prioridad:** Crítica
**Sprint:** 1

---

# HU-005: Dashboard de Progreso y Resumen Semanal

**Descripción:**
Como usuario, quiero visualizar un dashboard con mis métricas de progreso semanal (entrenamiento y nutrición) para evaluar mi adherencia y ajustar mi rutina.

**Criterios de Aceptación (DoD):**
- [ ] Dashboard muestra:
  - Total de sesiones completadas en la semana (X/4 o X/5)
  - Adherencia nutricional: % de días dentro del rango de calorías (±500 cal)
  - Volumen total de entrenamiento (suma de peso × reps × series)
  - Calorías promedio diarias de la semana
  - Macros promedio diarios de la semana
- [ ] Gráficos simples: línea de calorías diarias, volumen por día
- [ ] Comparativa: semana actual vs semana anterior
- [ ] Puede exportar resumen en PDF o compartir como imagen
- [ ] Validación: considerar solo días completados en cálculos

**Tareas Técnicas:**
- [ ] Crear DashboardFragment con RecyclerView/ViewPager
- [ ] Implementar queries en Room para agregación semanal
- [ ] Crear DashboardViewModel con cálculos de adherencia y volumen
- [ ] Integrar librería de gráficos (MPAndroidChart o Vico)
- [ ] Diseñar ResumenSemanalActivity
- [ ] Implementar comparación con semana anterior (query a 2 semanas atrás)
- [ ] Tests unitarios: agregaciones semanales, cálculos de adherencia

**Puntos de Historia:** L (8 puntos)
**Prioridad:** Alta
**Sprint:** 1

---

## Estimación T-Shirt Sizing

| Talla | Puntos |
|-------|--------|
| XS    | 3      |
| S     | 5      |
| M     | 8      |
| L     | 13     |
| XL    | 21     |

---

## Resumen Sprint 1

- **Total de Historias:** 5
- **Total de Puntos:** 60 puntos (13 + 13 + 8 + 13 + 13)
- **Prioridad Crítica:** 4 historias (HU-001 a HU-004)
- **Prioridad Alta:** 1 historia (HU-005)

### Labels Sugeridos para Issues
- `sprint-1`
- `tracker-entrenamiento`
- `nutricion`
- `critica`
- `mobile-d`
- `android`

### Tecnologías Clave
- **BD Local:** Room Database
- **UI:** XML layouts + Fragments
- **Autenticación:** Firebase Authentication o Backend propio
- **Persistencia de Sesión:** SharedPreferences / DataStore
- **Cálculos:** NutritionCalculator utility class
- **Gráficos:** MPAndroidChart o Vico
- **Testing:** JUnit4, Mockito, Espresso
