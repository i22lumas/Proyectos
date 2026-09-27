plugins {
    id("com.android.application")
    id("kotlin-android")
    id("jacoco")
}

android {
    namespace = "com.fitness.tracker"
    compileSdk = 34
    
    defaultConfig {
        applicationId = "com.fitness.tracker"
        minSdk = 24
        targetSdk = 34
        versionCode = 1
        versionName = "1.0.0"
        
        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }
    
    buildTypes {
        release {
            isMinifyEnabled = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
        debug {
            isMinifyEnabled = false
            enableUnitTestCoverage = true
        }
    }
    
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    
    kotlinOptions {
        jvmTarget = "17"
    }
    
    buildFeatures {
        buildConfig = true
    }
    
    testOptions {
        unitTests {
            isIncludeAndroidResources = true
            isReturnDefaultValues = true
        }
    }
}

dependencies {
    // Core Android
    implementation("androidx.core:core-ktx:1.12.0")
    implementation("androidx.appcompat:appcompat:1.6.1")
    implementation("com.google.android.material:material:1.10.0")
    implementation("androidx.constraintlayout:constraintlayout:2.1.4")
    
    // Jetpack Compose (opcional)
    implementation("androidx.compose.ui:ui:1.5.4")
    implementation("androidx.compose.material3:material3:1.1.1")
    
    // Networking
    implementation("com.squareup.okhttp3:okhttp:4.11.0")
    implementation("com.squareup.retrofit2:retrofit:2.9.0")
    implementation("com.squareup.retrofit2:converter-gson:2.9.0")
    
    // Database
    implementation("androidx.room:room-runtime:2.6.0")
    implementation("androidx.room:room-ktx:2.6.0")
    
    // Dependency Injection
    implementation("com.google.dagger:hilt-android:2.48")
    
    // Lifecycle
    implementation("androidx.lifecycle:lifecycle-runtime-ktx:2.6.2")
    implementation("androidx.lifecycle:lifecycle-viewmodel-ktx:2.6.2")
    
    // Testing
    testImplementation("junit:junit:4.13.2")
    testImplementation("org.mockito:mockito-core:5.3.1")
    testImplementation("org.mockito.kotlin:mockito-kotlin:5.1.0")
    testImplementation("androidx.test:core:1.5.0")
    testImplementation("androidx.test.ext:junit:1.1.5")
    testImplementation("org.robolectric:robolectric:4.10.3")
    
    androidTestImplementation("androidx.test.espresso:espresso-core:3.5.1")
    androidTestImplementation("androidx.test.ext:junit:1.1.5")
}

// Jacoco para coverage
jacoco {
    toolVersion = "0.8.10"
}

tasks.register("jacocoTestReport") {
    dependsOn("testDebugUnitTest")
    
    doLast {
        val fileFilter = setOf(
            "**/R.class",
            "**/R\$*.class",
            "**/*Test*.class",
            "**/BuildConfig.*",
            "**/Manifest*.*"
        )
        val tree = fileTree("${project.buildDir}/intermediates/classes/debug") {
            exclude(fileFilter)
        }
        
        val executionData = fileTree(project.buildDir) {
            include("**/*.exec", "**/*.ec")
        }
        
        println("Jacoco Report generado en: ${project.buildDir}/reports/jacoco/")
    }
}
