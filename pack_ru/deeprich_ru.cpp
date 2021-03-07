#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <regex>
#include <string>


// Функция, помогающая разделить слова по заданному символу
std::vector<std::string> Split(const std::string& target, char delimiter) {
    // istringstream - удобное средство для просмотра строки без ее изменения
    std::istringstream iss(target);
    std::string item;
    std::vector<std::string> words;
    // Считали из строки до разделителя
    while (std::getline(iss, item, delimiter)) {
        // создаем вектор разделенных слов
        words.push_back(item);
    }
    return words;
}

void SaveToMap(const std::vector<std::string>& input,
               std::map<std::string, size_t>& output) {
    for (const auto& word: input) {
        auto pair = output.insert(std::pair<std::string, size_t>(word, 1));
        if (!pair.second) {
            // Создаем пару - слово и количество вхождений в текст
            // Пушим в мапу, если такого слова нет - то количество вхождений - 1
            // иначе увеличиваем на один
            pair.first->second += 1;
        }
    }
}
std::map<std::string, size_t> ExtractText(const std::string& filePath) {
    std::ifstream file(filePath);
    std::map<std::string, size_t> words;
    if (!file.is_open()) {
        std::cout << "file is not opened" << std::endl;
        file.close();
        return words;
    }

    std::string line;
    while(std::getline(file, line)) {
        SaveToMap(Split(line, ' '), words);
    }
    return words;
}

bool IsParticiple(const std::string& word, const std::vector<std::regex>& patterns) {
    std::smatch sm;
    for (const auto& pattern : patterns) {
        if (std::regex_match(word, sm, pattern)) {
            return true;
        }
    }
    return false;
}
std::map<std::string, size_t> FilterParticiples(std::map<std::string, size_t>& words, const std::vector<std::regex>& patterns) {
    std::map<std::string, size_t> answer;
    for (const auto& word : words) {
        if (IsParticiple(word.first, patterns)) {
            answer.insert(word);
        }
    }
    return answer;
}

void SaveText(const std::map<std::string, size_t>& words,
                const std::string& fileName) {
    std::ofstream out (fileName);
    if (!out.is_open()) {
        std::cout << "file is not opened";
        return;
    }

    for (auto const& word : words) {
        out << "Деепричастие " << word.first << " встречается " << word.second
            << "  раз" << std::endl;
    }

    out.close();
}

const std::string path_to_input("/home/daniel/BMSTU/find_participle/input.txt");
const std::string path_to_output("/home/daniel/BMSTU/find_participle/output.txt");

int main() {
    static std::regex participle1("^.*?(вш).*$");
    static std::regex participle2("^.*?(ав)$");
    static std::regex participle3("^.*?(яв)$");
    static std::regex participle4("^.*?(ув)$");
    static std::regex participle5("^.*?(вши).*$");
    static std::regex participle6("^.*?(ши)$");
    static std::regex participle7("^.*?(ясь)$");
    static std::regex participle8("^.*?(ив)$");
    static std::regex participle9("^.*?(учи)$");
    static std::regex participle10("^.*?(ючи)$");

    std::vector<std::regex> participles {
        participle1
        , participle2
        , participle3
        , participle4
        , participle5
        , participle6
        , participle7
        , participle8
        , participle9
        , participle10
    };

    auto words = ExtractText(path_to_input);
    auto result = FilterParticiples(words, participles);
    SaveText(result, path_to_output);
    return 0;
}
