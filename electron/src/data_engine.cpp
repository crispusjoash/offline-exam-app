#include <napi.h>
#include <fstream>
#include <sstream>
#include <string>

Napi::String GetExamPaper(const Napi::CallbackInfo& info) {
    Napi::Env env = info.Env();

    if (info.Length() < 1 || !info[0].IsString()) {
        Napi::TypeError::New(env, "String expected").ThrowAsJavaScriptException();
        return Napi::String::New(env, "");
    }

    std::string filePath = info[0].As<Napi::String>().Utf8Value();

    std::ifstream file(filePath, std::ios::in | std::ios::binary);
    if (!file.is_open()) {
        Napi::Error::New(env, "Failed to open file: " + filePath).ThrowAsJavaScriptException();
        return Napi::String::New(env, "");
    }

    std::ostringstream contents;
    contents << file.rdbuf();
    file.close();

    return Napi::String::New(env, contents.str());
}

Napi::Object Init(Napi::Env env, Napi::Object exports) {
    exports.Set(Napi::String::New(env, "getExamPaper"),
                Napi::Function::New(env, GetExamPaper));
    return exports;
}

NODE_API_MODULE(data_engine, Init)
