css = """
<style>
.chat-message {
    margin: 15px 0;
    padding: 10px 15px;
    border-radius: 10px;
    max-width: 85%;
}
.user {
    background-color: #DCF8C6;
    align-self: flex-end;
    text-align: right;
    border: 1px solid #cce5b3;
}
.bot {
    background-color: #F1F0F0;
    align-self: flex-start;
    border: 1px solid #d3d3d3;
}
</style>
"""

user_template = """
<div class='chat-message user'>
    <strong>You:</strong><br>{{MSG}}
</div>
"""

bot_template = """
<div class='chat-message bot'>
    <strong>ReaderBuddy:</strong><br>{{MSG}}
</div>
"""

