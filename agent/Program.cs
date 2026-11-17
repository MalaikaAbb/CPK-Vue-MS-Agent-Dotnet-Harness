#pragma warning disable OPENAI001
using Microsoft.Extensions.AI;
                        using Microsoft.Agents.AI;

                        using Microsoft.Agents.AI.Hosting.AGUI.AspNetCore;
                        using OpenAI;
                        using OpenAI.Chat;

                        var builder = WebApplication.CreateBuilder(args);

                        builder.Services.AddAGUIServer();
                        var app = builder.Build();

                        var openAiApiKey = builder.Configuration["OPENAI_API_KEY"]
                            ?? throw new InvalidOperationException("Set OPENAI_API_KEY");
                        var openAI = new OpenAIClient(openAiApiKey);

                        var agent = openAI.GetChatClient("gpt-6-luna")
    .AsIChatClient().AsBuilder()
    .ConfigureOptions(options => options.RawRepresentationFactory = _ =>
        new OpenAI.Chat.ChatCompletionOptions { ReasoningEffortLevel = new("none") })
    .Build().AsAIAgent(
                            name: "MyAgent",
                            instructions: "You are a helpful assistant.");


                        app.MapAGUIServer("/", agent);
                        app.Run("http://localhost:8000");
