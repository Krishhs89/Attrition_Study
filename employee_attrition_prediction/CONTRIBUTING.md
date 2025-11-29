# Contributing to Employee Attrition Prediction

Thank you for your interest in contributing to this project! 🎉

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

---

## 🤝 Code of Conduct

This project adheres to a code of conduct that all contributors are expected to follow:

- **Be respectful** and inclusive
- **Be collaborative** and help others
- **Be professional** in all interactions
- **Focus on constructive feedback**

---

## 🚀 How Can I Contribute?

### Reporting Bugs

If you find a bug, please create an issue with:

- Clear, descriptive title
- Steps to reproduce the bug
- Expected vs actual behavior
- Your environment (OS, Python version, etc.)
- Screenshots if applicable

**Template:**
```markdown
**Bug Description:**
A clear description of the bug.

**To Reproduce:**
1. Run command '...'
2. Navigate to '...'
3. See error

**Expected Behavior:**
What you expected to happen.

**Environment:**
- OS: [e.g., macOS 13.0]
- Python: [e.g., 3.9.0]
- Dependencies: [e.g., Streamlit 1.28.0]
```

### Suggesting Enhancements

Enhancement suggestions are welcome! Please include:

- Clear use case
- Why this enhancement would be useful
- Possible implementation approach
- Alternatives you've considered

### Code Contributions

We welcome contributions in these areas:

1. **Machine Learning**
   - Implement new algorithms (Random Forest, XGBoost, Neural Networks)
   - Add SHAP explanations
   - Improve feature engineering
   - Hyperparameter tuning

2. **Data Processing**
   - Add data validation
   - Implement data quality checks
   - Support additional data formats
   - Add data sampling strategies

3. **Dashboards**
   - New visualizations
   - Enhanced interactivity
   - Mobile responsiveness
   - Performance optimizations

4. **Infrastructure**
   - Add unit tests
   - Improve CI/CD pipeline
   - Add integration tests
   - Docker improvements

5. **Documentation**
   - Fix typos
   - Add examples
   - Improve clarity
   - Translate to other languages

---

## 💻 Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/employee-attrition-prediction.git
cd employee-attrition-prediction
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # If exists

# Or for dashboard development
pip install streamlit pandas plotly pytest black flake8
```

### 4. Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html
```

### 5. Verify Setup

```bash
# Generate data
cd src
python generate_data.py

# Train model
python train_model.py

# Launch dashboard
streamlit run streamlit_app.py
```

---

## 📏 Coding Standards

### Python Style Guide

We follow [PEP 8](https://pep8.org/) with some modifications:

- **Line length**: 100 characters (not 79)
- **Indentation**: 4 spaces
- **Quotes**: Double quotes for strings
- **Docstrings**: Google style

### Code Formatting

Use `black` for automatic formatting:

```bash
# Format all Python files
black src/

# Check without modifying
black --check src/
```

### Linting

Use `flake8` to check code quality:

```bash
flake8 src/ --max-line-length=100
```

### Type Hints

Use type hints for function signatures:

```python
def predict_attrition(features: dict) -> float:
    """
    Predict attrition probability for an employee.
    
    Args:
        features: Dictionary of employee features
        
    Returns:
        Probability of attrition (0-1)
    """
    pass
```

### Docstrings

All public functions should have docstrings:

```python
def one_hot_encode(data, categorical_columns):
    """
    Apply one-hot encoding to categorical columns.
    
    Args:
        data (list): List of data rows
        categorical_columns (list): Column indices to encode
    
    Returns:
        tuple: (encoded_data, feature_names)
    
    Example:
        >>> data = [['M', 25], ['F', 30]]
        >>> encoded, names = one_hot_encode(data, [0])
        >>> print(names)
        ['gender_M', 'gender_F', 'age']
    """
    pass
```

---

## 📝 Commit Guidelines

### Commit Message Format

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**

```bash
feat(dashboard): add ROC curve visualization

Added interactive ROC curve plot to validation tab.
Includes AUC score display and threshold slider.

Closes #42
```

```bash
fix(model): correct one-hot encoding for new categories

Fixed bug where unseen categories in test set caused errors.
Now handles unknown values gracefully.
```

```bash
docs(readme): update installation instructions

Added troubleshooting section for common pip errors.
```

### Commit Best Practices

- Write clear, concise commit messages
- Keep commits atomic (one logical change per commit)
- Reference issues/PRs when relevant
- Don't commit sensitive data or credentials
- Test before committing

---

## 🔄 Pull Request Process

### Before Submitting

1. **Create a feature branch:**
   ```bash
   git checkout -b feat/my-new-feature
   ```

2. **Make your changes**
   - Follow coding standards
   - Add tests if applicable
   - Update documentation

3. **Test thoroughly:**
   ```bash
   pytest
   black --check src/
   flake8 src/
   ```

4. **Commit changes:**
   ```bash
   git add .
   git commit -m "feat(scope): description"
   ```

5. **Push to your fork:**
   ```bash
   git push origin feat/my-new-feature
   ```

### Submitting the PR

1. Go to the original repository on GitHub
2. Click "New Pull Request"
3. Select your fork and branch
4. Fill out the PR template:

```markdown
## Description
Brief description of changes

## Motivation
Why is this change needed?

## Changes Made
- List of changes
- Item 2
- Item 3

## Testing
How was this tested?

## Screenshots (if applicable)
Add screenshots here

## Checklist
- [ ] Code follows style guidelines
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] All tests passing
- [ ] No merge conflicts
```

### Review Process

1. **Automated checks** (CI/CD) must pass
2. **Code review** by maintainers
3. **Address feedback** if requested
4. **Approval** from at least one maintainer
5. **Merge** by maintainers

---

## 🧪 Testing Guidelines

### Writing Tests

All new features should include tests:

```python
# tests/test_model.py
def test_one_hot_encoding():
    """Test one-hot encoding generates correct features."""
    data = [['M', 25], ['F', 30]]
    encoded, names = one_hot_encode(data, [0])
    
    assert len(names) == 3  # gender_M, gender_F, age
    assert 'gender_M' in names
    assert encoded[0][0] == 1  # First row is Male
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_model.py

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=src --cov-report=html
```

---

## 📚 Documentation Guidelines

### Code Comments

- Explain **why**, not **what**
- Use comments for complex logic
- Keep comments up to date

### README Updates

When adding features, update:
- Installation instructions
- Usage examples
- API documentation
- Troubleshooting section

### Changelog

Update `CHANGELOG.md` following [Keep a Changelog](https://keepachangelog.com/):

```markdown
## [Unreleased]

### Added
- New feature X (#123)

### Fixed
- Bug in feature Y (#124)
```

---

## 🎯 Project Priorities

Current priorities (check GitHub issues for details):

1. **High Priority**
   - Add unit tests (coverage < 50%)
   - Implement SHAP explanations
   - Add data validation layer

2. **Medium Priority**
   - Support real HR data formats
   - Improve dashboard performance
   - Add more ML algorithms

3. **Low Priority**
   - Mobile dashboard support
   - API rate limiting
   - Internationalization

---

## ❓ Questions?

- **General questions:** Open a GitHub Discussion
- **Bug reports:** Create an issue
- **Feature requests:** Create an issue with `enhancement` label
- **Security issues:** Email maintainers directly (see README)

---

## 🙏 Recognition

All contributors will be:
- Listed in `README.md`
- Mentioned in release notes
- Recognized in the community

Thank you for contributing! 🎉

---

**Last Updated:** 2025-01-26
**Version:** 1.0
