// Top-level build file where you can add configuration options common to all sub-projects/modules.

plugins {
    id("com.android.application") version "8.1.0" apply false
    id("com.android.library") version "8.1.0" apply false
    id("org.jetbrains.kotlin.android") version "1.9.0" apply false
    id("org.sonarqube") version "4.4.1.3373"
}

// Configuración de SonarQube
sonarqube {
    properties {
        property("sonar.projectKey", "i22lumas_Proyectos_AppMovil")
        property("sonar.projectName", "Fitness Tracker - Android App")
        property("sonar.sourceEncoding", "UTF-8")
        property("sonar.sources", "src/main/java,src/main/kotlin")
        property("sonar.tests", "src/test/java,src/test/kotlin")
    }
}

tasks.register("clean", Delete::class) {
    delete(rootProject.buildDir)
}
