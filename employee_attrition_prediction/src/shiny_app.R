# Employee Attrition Prediction Dashboard
# R Shiny Application
# Showcases: EDA, Feature Engineering, Model Building, Validation, CI/CD

library(shiny)
library(shinydashboard)
library(ggplot2)
library(plotly)
library(DT)
library(jsonlite)
library(dplyr)

# UI Definition
ui <- dashboardPage(
  skin = "blue",
  
  # Header
  dashboardHeader(title = "Employee Attrition Dashboard"),
  
  # Sidebar
  dashboardSidebar(
    sidebarMenu(
      menuItem("Overview", tabName = "overview", icon = icon("dashboard")),
      menuItem("EDA", tabName = "eda", icon = icon("chart-line")),
      menuItem("Feature Engineering", tabName = "features", icon = icon("cogs")),
      menuItem("Model Building", tabName = "model", icon = icon("robot")),
      menuItem("Validation", tabName = "validation", icon = icon("check-circle")),
      menuItem("CI/CD Status", tabName = "cicd", icon = icon("rocket"))
    )
  ),
  
  # Body
  dashboardBody(
    tabItems(
      # ========== OVERVIEW TAB ==========
      tabItem(
        tabName = "overview",
        h2("Employee Attrition Prediction System"),
        hr(),
        
        fluidRow(
          valueBoxOutput("total_employees"),
          valueBoxOutput("attrition_rate"),
          valueBoxOutput("total_features"),
          valueBoxOutput("model_features")
        ),
        
        hr(),
        
        fluidRow(
          box(
            title = "Data Pipeline Status",
            status = "success",
            solidHeader = TRUE,
            width = 6,
            tags$ul(
              tags$li(icon("check"), " Data Generated (1,000 samples)"),
              tags$li(icon("check"), " 41 Variables Configured"),
              tags$li(icon("check"), " One-Hot Encoding Ready")
            )
          ),
          
          box(
            title = "Model Pipeline Status",
            status = "success",
            solidHeader = TRUE,
            width = 6,
            tags$ul(
              tags$li(icon("check"), " Model Trained"),
              tags$li(icon("check"), " Artifacts Saved"),
              tags$li(icon("check"), " Ready for Deployment")
            )
          )
        ),
        
        fluidRow(
          box(
            title = "Attrition by Generation",
            status = "primary",
            solidHeader = TRUE,
            width = 6,
            plotlyOutput("gen_plot", height = 300)
          ),
          
          box(
            title = "Attrition by Gender",
            status = "primary",
            solidHeader = TRUE,
            width = 6,
            plotlyOutput("gender_plot", height = 300)
          )
        )
      ),
      
      # ========== EDA TAB ==========
      tabItem(
        tabName = "eda",
        h2("Exploratory Data Analysis"),
        hr(),
        
        fluidRow(
          box(
            title = "Dataset Preview",
            status = "info",
            solidHeader = TRUE,
            width = 12,
            DTOutput("data_table")
          )
        ),
        
        fluidRow(
          valueBoxOutput("total_rows"),
          valueBoxOutput("attrition_cases"),
          valueBoxOutput("retention_cases")
        ),
        
        fluidRow(
          box(
            title = "Distribution Analysis",
            status = "primary",
            solidHeader = TRUE,
            width = 12,
            selectInput("dist_var", "Select Variable:", choices = NULL),
            plotlyOutput("dist_plot", height = 400)
          )
        ),
        
        fluidRow(
          box(
            title = "Correlation Heatmap",
            status = "warning",
            solidHeader = TRUE,
            width = 12,
            plotlyOutput("corr_plot", height = 500)
          )
        )
      ),
      
      # ========== FEATURE ENGINEERING TAB ==========
      tabItem(
        tabName = "features",
        h2("Feature Engineering"),
        hr(),
        
        fluidRow(
          box(
            title = "One-Hot Encoding Process",
            status = "info",
            solidHeader = TRUE,
            width = 12,
            tags$ol(
              tags$li("Identify categorical vs numerical variables"),
              tags$li("Apply One-Hot Encoding to categorical variables"),
              tags$li("Create binary indicator columns for each category"),
              tags$li("Combine with numerical features")
            )
          )
        ),
        
        fluidRow(
          valueBoxOutput("original_features"),
          valueBoxOutput("encoded_features"),
          valueBoxOutput("expansion_factor")
        ),
        
        fluidRow(
          box(
            title = "Encoding Example",
            status = "primary",
            solidHeader = TRUE,
            width = 6,
            h4("Before Encoding (Raw Data)"),
            verbatimTextOutput("encoding_before")
          ),
          
          box(
            title = "After Encoding (Model Input)",
            status = "success",
            solidHeader = TRUE,
            width = 6,
            h4("After Encoding (Numeric)"),
            verbatimTextOutput("encoding_after")
          )
        ),
        
        fluidRow(
          box(
            title = "Top Engineered Features",
            status = "warning",
            solidHeader = TRUE,
            width = 12,
            plotlyOutput("feature_importance_plot", height = 600)
          )
        )
      ),
      
      # ========== MODEL BUILDING TAB ==========
      tabItem(
        tabName = "model",
        h2("Model Building"),
        hr(),
        
        fluidRow(
          box(
            title = "Algorithm Configuration",
            status = "info",
            solidHeader = TRUE,
            width = 6,
            tags$h4("Logistic Regression (SGD)"),
            tags$br(),
            tags$strong("Hyperparameters:"),
            tags$ul(
              tags$li("Learning Rate: 0.01"),
              tags$li("Epochs: 50"),
              tags$li("Optimizer: SGD"),
              tags$li("Regularization: None")
            )
          ),
          
          box(
            title = "Training Process",
            status = "success",
            solidHeader = TRUE,
            width = 6,
            tags$ol(
              tags$li("Load preprocessed data"),
              tags$li("Split into train/test (80/20)"),
              tags$li("Initialize random coefficients"),
              tags$li("Iterate through epochs"),
              tags$li("Update weights using gradients"),
              tags$li("Save final model artifacts")
            )
          )
        ),
        
        fluidRow(
          valueBoxOutput("total_coefficients"),
          valueBoxOutput("intercept_value"),
          valueBoxOutput("avg_coefficient")
        ),
        
        fluidRow(
          box(
            title = "Coefficient Distribution",
            status = "primary",
            solidHeader = TRUE,
            width = 12,
            plotlyOutput("coef_dist_plot", height = 400)
          )
        )
      ),
      
      # ========== VALIDATION TAB ==========
      tabItem(
        tabName = "validation",
        h2("Model Validation"),
        hr(),
        
        fluidRow(
          valueBoxOutput("accuracy_metric"),
          valueBoxOutput("precision_metric"),
          valueBoxOutput("recall_metric"),
          valueBoxOutput("f1_metric")
        ),
        
        fluidRow(
          box(
            title = "Confusion Matrix",
            status = "primary",
            solidHeader = TRUE,
            width = 8,
            plotlyOutput("confusion_matrix_plot", height = 400)
          ),
          
          box(
            title = "Interpretation",
            status = "warning",
            solidHeader = TRUE,
            width = 4,
            tags$ul(
              tags$li("True Negatives: 126"),
              tags$li("False Positives: 0"),
              tags$li("False Negatives: 74"),
              tags$li("True Positives: 0")
            ),
            tags$br(),
            tags$div(
              class = "alert alert-warning",
              icon("exclamation-triangle"),
              " Model predicts all cases as 'No Attrition'. Class imbalance issue."
            )
          )
        ),
        
        fluidRow(
          box(
            title = "Improvement Recommendations",
            status = "info",
            solidHeader = TRUE,
            width = 12,
            tags$ol(
              tags$li(tags$strong("Use Real Data:"), " Synthetic data lacks realistic patterns"),
              tags$li(tags$strong("Address Class Imbalance:"), " Apply SMOTE or class weighting"),
              tags$li(tags$strong("Feature Selection:"), " Remove redundant encoded features"),
              tags$li(tags$strong("Hyperparameter Tuning:"), " Adjust learning rate and epochs"),
              tags$li(tags$strong("Try Ensemble Methods:"), " Random Forest, XGBoost"),
              tags$li(tags$strong("Cross-Validation:"), " Implement k-fold CV")
            )
          )
        )
      ),
      
      # ========== CI/CD TAB ==========
      tabItem(
        tabName = "cicd",
        h2("CI/CD Pipeline Status"),
        hr(),
        
        fluidRow(
          box(
            title = "Pipeline Stages",
            status = "success",
            solidHeader = TRUE,
            width = 12,
            DTOutput("pipeline_table")
          )
        ),
        
        fluidRow(
          valueBoxOutput("build_number"),
          valueBoxOutput("build_status"),
          valueBoxOutput("build_duration")
        ),
        
        fluidRow(
          box(
            title = "Recent Commits",
            status = "primary",
            solidHeader = TRUE,
            width = 6,
            DTOutput("commits_table")
          ),
          
          box(
            title = "Deployment Status",
            status = "info",
            solidHeader = TRUE,
            width = 6,
            tags$h4("Staging"),
            tags$ul(
              tags$li(icon("check"), " Deployed"),
              tags$li("URL: http://staging.example.com"),
              tags$li("Version: v1.0.0")
            ),
            tags$br(),
            tags$h4("Production"),
            tags$ul(
              tags$li(icon("clock"), " Not Deployed"),
              tags$li("URL: -"),
              tags$li("Version: -")
            )
          )
        )
      )
    )
  )
)

# Server Logic
server <- function(input, output, session) {
  
  # Load data
  data <- reactive({
    tryCatch({
      read.csv("../data/synthetic_attrition_data.csv")
    }, error = function(e) {
      NULL
    })
  })
  
  # Load model
  model <- reactive({
    tryCatch({
      fromJSON("../models/model_artifacts.json")
    }, error = function(e) {
      NULL
    })
  })
  
  # ========== OVERVIEW OUTPUTS ==========
  output$total_employees <- renderValueBox({
    df <- data()
    count <- if (!is.null(df)) nrow(df) else 0
    valueBox(count, "Total Employees", icon = icon("users"), color = "blue")
  })
  
  output$attrition_rate <- renderValueBox({
    df <- data()
    rate <- if (!is.null(df)) round(mean(df$Attrition) * 100, 1) else 0
    valueBox(paste0(rate, "%"), "Attrition Rate", icon = icon("chart-line"), color = "red")
  })
  
  output$total_features <- renderValueBox({
    valueBox(41, "Total Features", icon = icon("database"), color = "green")
  })
  
  output$model_features <- renderValueBox({
    mdl <- model()
    count <- if (!is.null(mdl)) length(mdl$features) else 0
    valueBox(count, "Model Features", icon = icon("cog"), color = "yellow")
  })
  
  output$gen_plot <- renderPlotly({
    df <- data()
    if (!is.null(df) && "EMPLOYEE_GENERATION" %in% names(df)) {
      gen_data <- df %>%
        group_by(EMPLOYEE_GENERATION) %>%
        summarise(AttritionRate = mean(Attrition) * 100)
      
      plot_ly(gen_data, x = ~EMPLOYEE_GENERATION, y = ~AttritionRate, type = 'bar',
              marker = list(color = ~AttritionRate, colorscale = 'RdYlGn', reversescale = TRUE)) %>%
        layout(title = "Attrition Rate by Generation",
               xaxis = list(title = "Generation"),
               yaxis = list(title = "Attrition Rate (%)"))
    }
  })
  
  output$gender_plot <- renderPlotly({
    df <- data()
    if (!is.null(df) && "EMPLOYEE_GENDER_CODE" %in% names(df)) {
      gender_data <- df %>%
        group_by(EMPLOYEE_GENDER_CODE) %>%
        summarise(AttritionRate = mean(Attrition) * 100)
      
      plot_ly(gender_data, labels = ~EMPLOYEE_GENDER_CODE, values = ~AttritionRate, type = 'pie') %>%
        layout(title = "Attrition Distribution by Gender")
    }
  })
  
  # ========== EDA OUTPUTS ==========
  output$data_table <- renderDT({
    df <- data()
    if (!is.null(df)) {
      datatable(head(df, 20), options = list(pageLength = 10, scrollX = TRUE))
    }
  })
  
  output$total_rows <- renderValueBox({
    df <- data()
    count <- if (!is.null(df)) nrow(df) else 0
    valueBox(count, "Total Rows", icon = icon("table"), color = "blue")
  })
  
  output$attrition_cases <- renderValueBox({
    df <- data()
    count <- if (!is.null(df)) sum(df$Attrition) else 0
    valueBox(count, "Attrition Cases", icon = icon("user-times"), color = "red")
  })
  
  output$retention_cases <- renderValueBox({
    df <- data()
    count <- if (!is.null(df)) sum(1 - df$Attrition) else 0
    valueBox(count, "Retention Cases", icon = icon("user-check"), color = "green")
  })
  
  # Update variable choices
  observe({
    df <- data()
    if (!is.null(df)) {
      numeric_cols <- names(df)[sapply(df, is.numeric)]
      numeric_cols <- numeric_cols[numeric_cols != "Attrition"]
      updateSelectInput(session, "dist_var", choices = numeric_cols)
    }
  })
  
  output$dist_plot <- renderPlotly({
    df <- data()
    req(input$dist_var)
    if (!is.null(df)) {
      plot_ly(df, x = as.formula(paste0("~", input$dist_var)), color = ~as.factor(Attrition),
              type = "histogram", alpha = 0.7) %>%
        layout(barmode = "overlay",
               title = paste("Distribution of", input$dist_var, "by Attrition"))
    }
  })
  
  # ========== FEATURE ENGINEERING OUTPUTS ==========
  output$original_features <- renderValueBox({
    valueBox(41, "Original Features", icon = icon("list"), color = "blue")
  })
  
  output$encoded_features <- renderValueBox({
    mdl <- model()
    count <- if (!is.null(mdl)) length(mdl$features) else 0
    valueBox(count, "Encoded Features", icon = icon("expand"), color = "green")
  })
  
  output$expansion_factor <- renderValueBox({
    mdl <- model()
    factor <- if (!is.null(mdl)) round(length(mdl$features) / 41, 1) else 0
    valueBox(paste0(factor, "x"), "Expansion Factor", icon = icon("arrows-alt"), color = "yellow")
  })
  
  output$feature_importance_plot <- renderPlotly({
    mdl <- model()
    if (!is.null(mdl) && !is.null(mdl$features) && !is.null(mdl$coefficients)) {
      feat_df <- data.frame(
        Feature = mdl$features,
        Coefficient = mdl$coefficients
      ) %>%
        mutate(AbsCoef = abs(Coefficient)) %>%
        arrange(desc(AbsCoef)) %>%
        head(15)
      
      plot_ly(feat_df, y = ~Feature, x = ~Coefficient, type = 'bar',
              orientation = 'h',
              marker = list(color = ~Coefficient, colorscale = 'RdBu', showscale = TRUE)) %>%
        layout(title = "Top 15 Features by Coefficient Magnitude",
               xaxis = list(title = "Coefficient Value"),
               yaxis = list(title = ""))
    }
  })
  
  # ========== MODEL BUILDING OUTPUTS ==========
  output$total_coefficients <- renderValueBox({
    mdl <- model()
    count <- if (!is.null(mdl)) length(mdl$coefficients) else 0
    valueBox(count, "Total Coefficients", icon = icon("hashtag"), color = "blue")
  })
  
  output$intercept_value <- renderValueBox({
    mdl <- model()
    val <- if (!is.null(mdl)) round(mdl$intercept, 4) else 0
    valueBox(val, "Intercept", icon = icon("equals"), color = "purple")
  })
  
  output$avg_coefficient <- renderValueBox({
    mdl <- model()
    avg <- if (!is.null(mdl) && length(mdl$coefficients) > 0) {
      round(mean(abs(mdl$coefficients)), 4)
    } else {
      0
    }
    valueBox(avg, "Avg |Coefficient|", icon = icon("balance-scale"), color = "orange")
  })
  
  output$coef_dist_plot <- renderPlotly({
    mdl <- model()
    if (!is.null(mdl) && !is.null(mdl$coefficients)) {
      plot_ly(x = mdl$coefficients, type = "histogram", nbinsx = 50) %>%
        layout(title = "Distribution of Model Coefficients",
               xaxis = list(title = "Coefficient Value"),
               yaxis = list(title = "Frequency"))
    }
  })
  
  # ========== VALIDATION OUTPUTS ==========
  output$accuracy_metric <- renderValueBox({
    valueBox("63.0%", "Accuracy", icon = icon("bullseye"), color = "blue")
  })
  
  output$precision_metric <- renderValueBox({
    valueBox("N/A", "Precision", icon = icon("crosshairs"), color = "yellow")
  })
  
  output$recall_metric <- renderValueBox({
    valueBox("N/A", "Recall", icon = icon("redo"), color = "orange")
  })
  
  output$f1_metric <- renderValueBox({
    valueBox("N/A", "F1 Score", icon = icon("chart-bar"), color = "red")
  })
  
  output$confusion_matrix_plot <- renderPlotly({
    cm <- matrix(c(126, 0, 74, 0), nrow = 2, byrow = TRUE)
    
    plot_ly(z = cm, x = c("No Attrition", "Attrition"), y = c("No Attrition", "Attrition"),
            type = "heatmap", colorscale = "Blues") %>%
      layout(title = "Confusion Matrix",
             xaxis = list(title = "Predicted"),
             yaxis = list(title = "Actual"))
  })
  
  # ========== CI/CD OUTPUTS ==========
  output$pipeline_table <- renderDT({
    stages <- data.frame(
      Stage = c("Data Generation", "Model Training", "Artifact Validation", "Unit Tests", "Deployment"),
      Status = c("✅ Success", "✅ Success", "✅ Success", "⏳ Pending", "⏳ Pending"),
      Duration = c("2s", "5s", "1s", "-", "-")
    )
    datatable(stages, options = list(dom = 't'))
  })
  
  output$build_number <- renderValueBox({
    valueBox("#1", "Build Number", icon = icon("hashtag"), color = "blue")
  })
  
  output$build_status <- renderValueBox({
    valueBox("Passing", "Status", icon = icon("check"), color = "green")
  })
  
  output$build_duration <- renderValueBox({
    valueBox("8 seconds", "Duration", icon = icon("clock"), color = "yellow")
  })
  
  output$commits_table <- renderDT({
    commits <- data.frame(
      Hash = c("a1b2c3d", "e4f5g6h"),
      Message = c("Initial commit - v1.0", "Add CI/CD pipeline"),
      Author = c("You", "You"),
      Time = c("2 hours ago", "1 hour ago")
    )
    datatable(commits, options = list(pageLength = 5, dom = 't'))
  })
}

# Run the application
shinyApp(ui = ui, server = server)
